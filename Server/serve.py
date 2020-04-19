from concurrent import futures
import grpc
import random

from comms import GameState_pb2
from comms import GameState_pb2_grpc


class GameServer(GameState_pb2_grpc.GameServiceServicer):

    def HelloWorld(self, request, context):
        return GameState_pb2.HelloWorldResponse(message="Hello {}".format(request.name))

    def GetInitialGameState(self, request, context):
        print("Configuring initial game state")
        player_id = str(random.randint(0, 100000))
        hand = [GameState_pb2.Card(index=random.randint(0, 5)) for i in range(5)]

        initial_state = GameState_pb2.GameState(
            turn_number=1,
            player_money=100,
            hand=hand,
            deck_size=35,
        )

        return GameState_pb2.InitialisationResponse(
            player_id=player_id,
            initial_state=initial_state
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GameState_pb2_grpc.add_GameServiceServicer_to_server(GameServer(), server)

    server.add_insecure_port("localhost:50051")
    server.start()
    print("Listening for messages")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
