import os
import sys
from concurrent import futures

import grpc
import highlight_io
from loguru import logger

from app.service import GreeterService
from app.servicer import Greeter
from com.grpc.services import hello_pb2_grpc

logger.remove()
logger.add(sys.stderr, level="INFO", serialize=True)

H = highlight_io.H(
    os.environ["HIGHLIGHT_IO_PROJECT_ID"],
    instrument_logging=False,
    service_name="my-app",
    service_version="git-sha",
)

logger.add(
    H.logging_handler,
    level="INFO",
    backtrace=True,
    serialize=True,
)


def serve():
    """Run GRPC server."""
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greter_service = GreeterService()
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(greter_service), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    logger.info(f"Server started, listening on {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
