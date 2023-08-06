from setuptools import setup, find_packages

setup(
    name="zmq_ai_client_python",
    version="0.2",
    packages=find_packages(),
    author="Fatih GENÇ",
    author_email="f.genc@qimia.de",
    description="A ZMQ client interface for llama server",
    long_description="A ZMQ client interface for llama server",
    url="http://github.com/zmq-ai-client-python",
    install_requires=[
        "pyzmq",
        "msgpack"
    ],
)
