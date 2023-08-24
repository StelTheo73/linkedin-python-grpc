# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.server import rides_pb2 as src_dot_server_dot_rides__pb2


class RidesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/Rides/Start',
                request_serializer=src_dot_server_dot_rides__pb2.StartRequest.SerializeToString,
                response_deserializer=src_dot_server_dot_rides__pb2.StartResponse.FromString,
                )
        self.Track = channel.stream_unary(
                '/Rides/Track',
                request_serializer=src_dot_server_dot_rides__pb2.TrackRequest.SerializeToString,
                response_deserializer=src_dot_server_dot_rides__pb2.TrackResponse.FromString,
                )


class RidesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Track(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RidesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=src_dot_server_dot_rides__pb2.StartRequest.FromString,
                    response_serializer=src_dot_server_dot_rides__pb2.StartResponse.SerializeToString,
            ),
            'Track': grpc.stream_unary_rpc_method_handler(
                    servicer.Track,
                    request_deserializer=src_dot_server_dot_rides__pb2.TrackRequest.FromString,
                    response_serializer=src_dot_server_dot_rides__pb2.TrackResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Rides', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Rides(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rides/Start',
            src_dot_server_dot_rides__pb2.StartRequest.SerializeToString,
            src_dot_server_dot_rides__pb2.StartResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Track(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Rides/Track',
            src_dot_server_dot_rides__pb2.TrackRequest.SerializeToString,
            src_dot_server_dot_rides__pb2.TrackResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)