from concurrent import futures
import grpc

from comms import GameState_pb2
from comms import GameState_pb2_grpc


class GameServer(GameState_pb2_grpc.GameServiceServicer):

    def HelloWorld(self, request, context):
        print("Received a request")
        return GameState_pb2.HelloWorldResponse(message="Hello {}".format(request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GameState_pb2_grpc.add_GameServiceServicer_to_server(GameServer(), server)

    server.add_insecure_port("localhost:50051")
    server.start()
    print("Listening for messages")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
