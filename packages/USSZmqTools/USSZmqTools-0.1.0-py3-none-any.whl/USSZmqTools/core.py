from __future__ import annotations
import logging
import zmq
import uuid
from typing import Dict, Generator, Optional, List, Tuple, Union

class BrokerWorker:
    def __init__(self, endpoint: str, identity: Optional[str] = None, socket_type=zmq.DEALER) -> None:
        """
        Initializes a BrokerConsumer object.

        Args:
            endpoint (str): The endpoint to connect to.
            identity (str, optional): The identity string. Defaults to None.
            socket_type (zmq.SocketType, optional): The socket type. Defaults to zmq.DEALER.
        """
        if identity is not None and not isinstance(identity, str):
            raise TypeError("identity must be a string")
        if not isinstance(endpoint, str):
            raise TypeError("endpoint must be a string")

        self.identity = identity.encode("ascii") if identity is not None else uuid.uuid4().hex.encode("ascii")
        self.socket = zmq.Context().socket(socket_type)
        self.socket.identity = self.identity

        try:
            self.socket.connect(endpoint)
            self._connect()
        except zmq.ZMQError as e:
            raise e

    def _connect(self) -> None:
        """
        Private method to connect the socket to the endpoint.
        """
        self.socket.send_multipart([b"JOIN", self.identity])

    def leave_broker(self) -> None:
        """
        Sends a LEAVE message to the broker and closes the socket.

        Parameters:
            self (obj): The instance of the class.
        
        Returns:
            None
        """
        self.socket.send_multipart([b"LEAVE", self.identity])
        self.socket.close()

    def send(self, data: bytes) -> None:
        """
        Sends the given data through the socket.

        Args:
            data (bytes): The data to be sent.

        Returns:
            None
        """
        self.socket.send(data)

    def get_message(self) -> List[bytes]:
        '''
        Retrieves multiple messages from the socket connection and returns them as a list of bytes.
        
        This is a blocking call, meaning it will wait until there are messages available to receive.
    
        Returns:
        List[bytes]: A list of bytes containing the messages received from the socket connection.
        '''
        return self.socket.recv_multipart()

    def listen(self) -> Generator[Tuple[bytes, bytes], None, None]:
        """
        Listen for incoming requests and yield a tuple of the address and request.
        This function is a generator that continuously listens for incoming requests.
        It receives a multipart message from the socket, extracts the address and request,
        and yields them as a tuple. It then sends a multipart message back to the broker,
        containing the address and the identity of the listener.

        Parameters:
        - None

        Returns:
        - A generator that yields a tuple of bytes representing the address and bytes representing the request.

        Raises:
        - zmq.ZMQError: If there is an error while receiving the multipart message.

        - GeneratorExit: If the generator is being closed.

        - KeyboardInterrupt: If the user interrupts the program with a keyboard interrupt.

        - SystemExit: If the program is being terminated.

        Note:
        - This function is designed to be used in a loop or with a `for` statement to continuously listen for requests.
        - When the generator is closed or an interrupt or termination signal is received, the function will return.
        """
        try:
            while True:
                try:
                    address, _, request = self.socket.recv_multipart()
                    yield address,request
                    self.socket.send_multipart([address,self.identity])
                except zmq.ZMQError as e:
                    raise e
        except GeneratorExit:
            return
        except (KeyboardInterrupt, SystemExit):
            self.leave_broker()
            return

class BrokerClient:
    def __init__(self, endpoint: str,identity: Optional[str] = None, socket_type=zmq.DEALER):
        """
        Initialize the BrokerProducer class.

        Args:
            endpoint (str): The endpoint to connect to.
            identity (str, optional): The identity of the socket. Defaults to None.
            socket_type (zmq.SocketType, optional): The type of socket to use. Defaults to zmq.DEALER.
        """
        if identity is not None and not isinstance(identity,str):
            raise TypeError("identity must be a string")
        if not isinstance(endpoint,str):
            raise TypeError("endpoint must be a string")
        
        self.identity = identity.encode("ascii") if identity is not None else uuid.uuid4().hex.encode("ascii")
        self.context = zmq.Context()
        self.socket = self.context.socket(socket_type)
        self.socket.identity = self.identity
        self.socket.connect(endpoint)

    def send(self, data: bytes):
        """
        Sends the given bytes over the socket.

        Args:
            data (bytes): The data to be sent.

        Returns:
            None
        """
        self.socket.send(data)

    def send_string(self, data: str) -> None:
        """
        Sends the given string through the socket.

        Args:
            data (str): The string to be sent.
        
        Returns:
            None
        """
        self.socket.send_string(data)

    def send_json(self, data: Dict[str, Union[str, int]]) -> None:
        """
        Sends the given json through the socket.

        Args:
            data (str): The json to be sent.
        
        Returns:
            None
        """
        self.socket.send_json(data)

    def close(self):
        """
        Closes the socket and terminates the context.

        Returns:
            None

        """
        self.socket.close()
        self.context.term()
        print("Closed")

class Broker:
    def __init__(self, frontend_port:int=5555, backend_port:int=5556, **kwargs):
        """
        Initialize the Broker class.

        Args:
            frontend_port (int): The port number for the frontend socket.
            backend_port (int): The port number for the backend socket.
            **kwargs: Additional keyword arguments.
        """
        self.frontend_port = frontend_port
        self.backend_port = backend_port
        self.max_log_string = kwargs.get("max_log_string", 100)
        self.shutdown = False
        LOGGING_MODE = kwargs.get("logging_mode", logging.INFO)
        logging.basicConfig(format='[%(asctime)s]-%(levelname)s-%(message)s', level=LOGGING_MODE, datefmt='%m-%d-%Y %H:%M:%S')
        self.logger = logging.getLogger(__name__)

        self.context = zmq.Context()
        self.frontend = self.context.socket(zmq.ROUTER)
        self.backend = self.context.socket(zmq.DEALER)

        try:
            self.logger.info(f"Binding frontend to {self.frontend_port} and backend to {self.backend_port}")
            self.frontend.bind(f"tcp://*:{self.frontend_port}")
            self.backend.bind(f"tcp://*:{self.backend_port}")
        except zmq.ZMQError as e:
            self.logger.error(f"Error binding sockets: {e}")
            raise SystemExit

        self.backend_ready = False
        self.workers = []
        self.poller = zmq.Poller()
        self.poller.register(self.backend, zmq.POLLIN)
        self.poller.register(self.frontend, zmq.POLLIN)
        self.logger.info("Broker started")

    def listen(self):
        """
        Listens for incoming requests from clients and worker activity on the backend.
        This function runs in a loop until the shutdown flag is set to True.
        
        Parameters:
            self (object): The instance of the class.
            
        Returns:
            None
        """

        while not self.shutdown:
            try:
                sockets = dict(self.poller.poll(timeout=4000))  # Timeout in milliseconds (100 ms)

                if self.backend in sockets:
                    # Handle worker activity on the backend
                    try:
                        request,worker = self.backend.recv_multipart()
                    except zmq.ZMQError as e:
                        self.logger.error(f"Error receiving multipart message on backend socket: {e}")
                        continue

                    if request == b'JOIN':
                        logging.info(f"Worker {worker.decode('utf-8')} connected")
                    elif request == b'LEAVE':
                        logging.info(f"Worker {worker.decode('utf-8')} disconnected")
                        if worker in self.workers:
                            self.workers.remove(worker)
                        continue
                    self.workers.append(worker)
                    if self.workers and not self.backend_ready:
                        # Poll for clients now that a worker is available and backend was not ready
                        self.poller.register(self.frontend, zmq.POLLIN)
                        self.backend_ready = True

                if self.frontend in sockets:
                    # Get next client request, route to last-used worker
                    client, request = self.frontend.recv_multipart()
                    # Log message received from client
                    log_request = request[:self.max_log_string] + b'...' if len(request) > self.max_log_string else request
                    
                    # This actually logs the time that it sends the message not the time it receives it
                    logging.info(f"Client {client.decode('utf-8')} sent request: {log_request}")
                    try:
                        # Get available worker
                        worker = self.workers.pop(0)
                    except IndexError as e:
                        logging.error(f'Client {client} request not processed. No workers in broker: {e}')
                        continue
                    # Send message to worker
                    self.backend.send_multipart([worker, client,request])
                    if not self.workers:
                        # Don't poll clients if no workers are available and set backend_ready flag to false
                        self.poller.unregister(self.frontend)
                        self.backend_ready = False
            except KeyboardInterrupt:
                break
            except Exception as e:
                logging.error(f"Error: {e}")
                break
            
        self.close()

    def close(self):
        """
        Closes the connection and shuts down the server.

        This method sets the `shutdown` flag to `True` to indicate that the server should be shut down. It then closes the frontend and backend connections, and terminates the context.

        Parameters:
            None

        Returns:
            None
        """
        logging.info("Terminating broker..")
        self.shutdown = True
        self.frontend.close()
        self.backend.close()
        self.context.term()

