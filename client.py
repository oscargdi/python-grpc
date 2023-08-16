import logging

import grpc

from com.grpc.messages import hello_pb2
from com.grpc.services import hello_pb2_grpc

logger = logging.getLogger(__name__)


def run():
    """Execute client request."""
    logger.info("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Oscar"))
    logger.info("Greeter client received: %s", response.message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
