# USSZmqTools

## Description
USSZmqTools is a Python library that provides easy-to-use classes for interacting with ZeroMQ (ZMQ) sockets. It includes the `Client`, `Worker`, and `Broker` classes to facilitate communication between clients and workers using the ZMQ pattern.

## Installation

You can install USSZmqTools using `pip`. Open your terminal or command prompt and run the following command:
```
pip install USSZmqTools
```

## Usage

### 1. Client Class

The `Client` class represents a client that interacts with the `Broker` to send requests.

```python
from USSZmqTools import BrokerClient

# Create a Client instance and connect to the Broker
client = BrokerClient(endpoint='tcp://localhost:5555')

# Send data as bytes
data = b'Hello from client'
client.send(data)

# Send data as a string
data_str = 'Hello as a string'
client.send_string(data_str)

# Send data as JSON
data_json = {'key': 'value', 'num': 42}
client.send_json(data_json)

# Close the connection
client.close()
```
### 2. Worker Class
The `Worker` class represents a worker that interacts with the `Broker` to process requests.

```python
from USSZmqTools import BrokerWorker

# Create a Worker instance and connect to the Broker
worker = BrokerWorker(endpoint='tcp://localhost:5556')

# Receive data as bytes
data = worker.recv()

# Receive data as a string
data_str = worker.recv_string()

# Receive data as JSON
data_json = worker.recv_json()

# Process the data...
print(data)
print(data_str)
print(data_json)

# Close the connection
worker.close()

```

You can also continuously get messages from the consumer by calling the `listen()` generator function like so:
```python
from USSZmqTools import BrokerWorker

# Create a Worker instance and connect to the Broker
worker = BrokerWorker(endpoint='tcp://localhost:5556')

count = 0
# Continuously get messages from the worker until 5 requests are received
for msg in worker.listen():
    # Do something with data..
    if count >= 5:
        break
    count += 1

# Close the connection
worker.close()

```

### 3. Broker Class
The `Broker` class acts as a mediator between clients and workers, routing requests to available workers.

```python
from USSZmqTools import Broker

# Create a Broker instance and start listening for requests
broker = Broker(frontend_port=5555, backend_port=5556)

# Start the broker (this runs in a loop until the shutdown flag is set to True)
broker.listen()

# Once the broker is no longer needed, close the connection and shut down the server
broker.close()

```
