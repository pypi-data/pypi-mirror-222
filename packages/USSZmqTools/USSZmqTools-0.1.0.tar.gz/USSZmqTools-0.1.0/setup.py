from setuptools import setup,find_packages

setup(
    name="USSZmqTools",
    version="0.1.0",
    description="A Python package implementing a broker-worker pattern using ZeroMQ for communication.",
    long_description="This package provides a basic implementation of a broker-worker pattern using ZeroMQ (ZMQ) for communication. It includes three classes: BrokerWorker, BrokerClient, and Broker. The BrokerWorker class represents a worker that connects to a broker endpoint using ZMQ. The BrokerClient class represents a client that connects to a broker endpoint using ZMQ. The Broker class represents the broker itself and handles communication between clients and workers. This package is suitable for building distributed systems or task queues.",
    long_description_content_type="text/markdown",
    url="https://github.com/USSVision/USSCommonTools/tree/main/Packages/USSZmqTools",
    author='USS Vision',
    author_email='bhelfer@ussvision.com',
    license='MIT',
    packages=find_packages(),
    install_requires=["pyzmq","wheel"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',         
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
