from app.service import Service
from com.grpc.messages import hello_pb2
from com.grpc.services import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    """Greeter implementation."""

    def __init__(self, service: Service) -> None:
        super().__init__()
        self.service = service

    def SayHello(self, request: hello_pb2.HelloRequest, context):
        message = self.service.get_greeting(request.name)
        return hello_pb2.HelloReply(message=message)
