import logging
from concurrent import futures

import grpc

from app.service import GreeterService
from app.servicer import Greeter
from com.grpc.services import hello_pb2_grpc

logger = logging.getLogger(__name__)


def serve():
    """Run GRPC server."""
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greter_service = GreeterService()
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(greter_service), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    logger.info("Server started, listening on %s", port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
