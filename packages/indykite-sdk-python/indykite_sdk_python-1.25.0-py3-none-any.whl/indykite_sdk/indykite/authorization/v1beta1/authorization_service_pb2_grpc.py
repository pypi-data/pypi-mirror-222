# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from indykite_sdk.indykite.authorization.v1beta1 import authorization_service_pb2 as indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2


class AuthorizationAPIStub(object):
    """AuthorizationAPI represents the service interface for authorization.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IsAuthorized = channel.unary_unary(
                '/indykite.authorization.v1beta1.AuthorizationAPI/IsAuthorized',
                request_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedRequest.SerializeToString,
                response_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedResponse.FromString,
                )
        self.WhatAuthorized = channel.unary_unary(
                '/indykite.authorization.v1beta1.AuthorizationAPI/WhatAuthorized',
                request_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedRequest.SerializeToString,
                response_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedResponse.FromString,
                )
        self.WhoAuthorized = channel.unary_unary(
                '/indykite.authorization.v1beta1.AuthorizationAPI/WhoAuthorized',
                request_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedRequest.SerializeToString,
                response_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedResponse.FromString,
                )


class AuthorizationAPIServicer(object):
    """AuthorizationAPI represents the service interface for authorization.
    """

    def IsAuthorized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhatAuthorized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhoAuthorized(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorizationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IsAuthorized': grpc.unary_unary_rpc_method_handler(
                    servicer.IsAuthorized,
                    request_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedRequest.FromString,
                    response_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedResponse.SerializeToString,
            ),
            'WhatAuthorized': grpc.unary_unary_rpc_method_handler(
                    servicer.WhatAuthorized,
                    request_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedRequest.FromString,
                    response_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedResponse.SerializeToString,
            ),
            'WhoAuthorized': grpc.unary_unary_rpc_method_handler(
                    servicer.WhoAuthorized,
                    request_deserializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedRequest.FromString,
                    response_serializer=indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'indykite.authorization.v1beta1.AuthorizationAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthorizationAPI(object):
    """AuthorizationAPI represents the service interface for authorization.
    """

    @staticmethod
    def IsAuthorized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indykite.authorization.v1beta1.AuthorizationAPI/IsAuthorized',
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedRequest.SerializeToString,
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.IsAuthorizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhatAuthorized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indykite.authorization.v1beta1.AuthorizationAPI/WhatAuthorized',
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedRequest.SerializeToString,
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhatAuthorizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhoAuthorized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indykite.authorization.v1beta1.AuthorizationAPI/WhoAuthorized',
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedRequest.SerializeToString,
            indykite_dot_authorization_dot_v1beta1_dot_authorization__service__pb2.WhoAuthorizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
