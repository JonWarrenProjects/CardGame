import grpc

from comms import GameState_pb2_grpc
from comms import GameState_pb2


def main():

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = GameState_pb2_grpc.GameServiceStub(channel)

        response = stub.HelloWorld(GameState_pb2.HelloWorldRequest(name="Jan Frederick"))
        print(response.message)


if __name__ == "__main__":
    main()
