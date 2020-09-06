# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import msg_pb2 as msg__pb2


class StorageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Save = channel.unary_unary(
                '/storage.StorageService/Save',
                request_serializer=msg__pb2.Data.SerializeToString,
                response_deserializer=msg__pb2.Req.FromString,
                )
        self.Load = channel.unary_unary(
                '/storage.StorageService/Load',
                request_serializer=msg__pb2.Req.SerializeToString,
                response_deserializer=msg__pb2.Data.FromString,
                )
        self.Remove = channel.unary_unary(
                '/storage.StorageService/Remove',
                request_serializer=msg__pb2.Req.SerializeToString,
                response_deserializer=msg__pb2.Req.FromString,
                )


class StorageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Load(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Save': grpc.unary_unary_rpc_method_handler(
                    servicer.Save,
                    request_deserializer=msg__pb2.Data.FromString,
                    response_serializer=msg__pb2.Req.SerializeToString,
            ),
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=msg__pb2.Req.FromString,
                    response_serializer=msg__pb2.Data.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=msg__pb2.Req.FromString,
                    response_serializer=msg__pb2.Req.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'storage.StorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StorageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Save',
            msg__pb2.Data.SerializeToString,
            msg__pb2.Req.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Load',
            msg__pb2.Req.SerializeToString,
            msg__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/storage.StorageService/Remove',
            msg__pb2.Req.SerializeToString,
            msg__pb2.Req.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
