import grpc

import GameState_pb2
import GameState_pb2_grpc


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = GameState_pb2_grpc.GameServiceStub(channel)

        response = stub.HelloWorld(GameState_pb2.HelloWorldRequest(name="Jan Frederick"))
        print(response.message)


if __name__ == "__main__":
    main()
