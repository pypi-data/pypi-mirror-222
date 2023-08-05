# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.generic_data_container_pb2 as generic__data__container__pb2


class GenericDataContainerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/Create',
                request_serializer=generic__data__container__pb2.CreateRequest.SerializeToString,
                response_deserializer=generic__data__container__pb2.GenericDataContainer.FromString,
                )
        self.SetProperty = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/SetProperty',
                request_serializer=generic__data__container__pb2.SetPropertyRequest.SerializeToString,
                response_deserializer=generic__data__container__pb2.SetPropertyResponse.FromString,
                )
        self.GetProperty = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetProperty',
                request_serializer=generic__data__container__pb2.GetPropertyRequest.SerializeToString,
                response_deserializer=generic__data__container__pb2.GetPropertyResponse.FromString,
                )
        self.GetPropertyTypes = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetPropertyTypes',
                request_serializer=generic__data__container__pb2.GetPropertyTypesRequest.SerializeToString,
                response_deserializer=generic__data__container__pb2.GetPropertyTypesResponse.FromString,
                )
        self.GetPropertyNames = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetPropertyNames',
                request_serializer=generic__data__container__pb2.GetPropertyNamesRequest.SerializeToString,
                response_deserializer=generic__data__container__pb2.GetPropertyNamesResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/Delete',
                request_serializer=generic__data__container__pb2.GenericDataContainer.SerializeToString,
                response_deserializer=base__pb2.Empty.FromString,
                )


class GenericDataContainerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPropertyTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPropertyNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GenericDataContainerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=generic__data__container__pb2.CreateRequest.FromString,
                    response_serializer=generic__data__container__pb2.GenericDataContainer.SerializeToString,
            ),
            'SetProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.SetProperty,
                    request_deserializer=generic__data__container__pb2.SetPropertyRequest.FromString,
                    response_serializer=generic__data__container__pb2.SetPropertyResponse.SerializeToString,
            ),
            'GetProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProperty,
                    request_deserializer=generic__data__container__pb2.GetPropertyRequest.FromString,
                    response_serializer=generic__data__container__pb2.GetPropertyResponse.SerializeToString,
            ),
            'GetPropertyTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPropertyTypes,
                    request_deserializer=generic__data__container__pb2.GetPropertyTypesRequest.FromString,
                    response_serializer=generic__data__container__pb2.GetPropertyTypesResponse.SerializeToString,
            ),
            'GetPropertyNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPropertyNames,
                    request_deserializer=generic__data__container__pb2.GetPropertyNamesRequest.FromString,
                    response_serializer=generic__data__container__pb2.GetPropertyNamesResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=generic__data__container__pb2.GenericDataContainer.FromString,
                    response_serializer=base__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ansys.api.dpf.generic_data_container.v0.GenericDataContainerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GenericDataContainerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/Create',
            generic__data__container__pb2.CreateRequest.SerializeToString,
            generic__data__container__pb2.GenericDataContainer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/SetProperty',
            generic__data__container__pb2.SetPropertyRequest.SerializeToString,
            generic__data__container__pb2.SetPropertyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetProperty',
            generic__data__container__pb2.GetPropertyRequest.SerializeToString,
            generic__data__container__pb2.GetPropertyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPropertyTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetPropertyTypes',
            generic__data__container__pb2.GetPropertyTypesRequest.SerializeToString,
            generic__data__container__pb2.GetPropertyTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPropertyNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/GetPropertyNames',
            generic__data__container__pb2.GetPropertyNamesRequest.SerializeToString,
            generic__data__container__pb2.GetPropertyNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ansys.api.dpf.generic_data_container.v0.GenericDataContainerService/Delete',
            generic__data__container__pb2.GenericDataContainer.SerializeToString,
            base__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
