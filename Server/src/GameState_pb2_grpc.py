# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from src import GameState_pb2 as src_dot_GameState__pb2


class GameServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloWorld = channel.unary_unary(
                '/GameService/HelloWorld',
                request_serializer=src_dot_GameState__pb2.HelloWorldRequest.SerializeToString,
                response_deserializer=src_dot_GameState__pb2.HelloWorldResponse.FromString,
                )


class GameServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def HelloWorld(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloWorld,
                    request_deserializer=src_dot_GameState__pb2.HelloWorldRequest.FromString,
                    response_serializer=src_dot_GameState__pb2.HelloWorldResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def HelloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GameService/HelloWorld',
            src_dot_GameState__pb2.HelloWorldRequest.SerializeToString,
            src_dot_GameState__pb2.HelloWorldResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
