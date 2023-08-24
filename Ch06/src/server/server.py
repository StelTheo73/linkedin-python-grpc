""" Simple grpc server
Run from Ch06 folder with python3 server_main.py
"""

from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4
from socket import socket
from time import perf_counter

from grpc_reflection.v1alpha import reflection
from src.libraries.validate import InvalidFieldError

import grpc
import src.libraries.config as config
import src.libraries.log as log
import src.server.rides_pb2 as pb
import src.server.rides_pb2_grpc as rpc

def new_ride_id() -> str:
    """ Returns a random UUID in hex format. """
    return uuid4().hex

def load_credentials():
    """ Loads credentials"""
    with open(config.CERT_FILE, 'rb') as fp:
        cert = fp.read()

    with open(config.KEY_FILE, 'rb') as fp:
        key = fp.read()

    return grpc.ssl_server_credentials([(key, cert)])

def get_free_port():
    """ Returns a free port """
    with socket() as sock:
        sock.bind(("localhost", 0))
        _, port = sock.getsockname()
        return port

def build_server(port, secure=False):
    # Create generic grpc server (our server)
    server = grpc.server(
        ThreadPoolExecutor(),
        interceptors=[TimingInterceptor()]
    )
    # Register our server inside grpc server (from rpc module)
    rpc.add_RidesServicer_to_server(Rides(), server)

    # Reflection: external clients can query the server
    # about the available methods and types
    names = (
        pb.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(names, server)

    address = f"[::]:{port}"

    if secure == True:
        credentials = load_credentials()
        # Force grpc to use HTTPS
        server.add_secure_port(address, credentials)
    else:
        server.add_insecure_port(address)

    return server

class Rides(rpc.RidesServicer):
    """ Rides Servicer class """

    def Start(self, request, context) -> pb.StartResponse:
        log.info(f"ride: {request}")
        log.info(f"context: {context}")

        try:
            Rides.validate_request(request)
        except InvalidFieldError as err:
            log.error("bad request: {err}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f"{err.field} is {err.reason}")
            raise err

        # TODO (steltheo73): Store ride in database
        ride_id = new_ride_id()
        return pb.StartResponse(id=ride_id)

    def Track(self, request_iterator, context):
        count = 0
        for request in request_iterator:
            # TODO (steltheo73): Store in database
            log.info(f"track: {request}")
            log.info(f"context: {context}")
            count += 1

        return pb.TrackResponse(count=count)

    @staticmethod
    def validate_request(request):
        if not request.driver_id:
            raise InvalidFieldError("driver_id", "empty")
        # TODO (steltheo73): Validate more fields

class TimingInterceptor(grpc.ServerInterceptor):
    """ Middleware (does nothing) """

    def intercept_service(self, continuation, handler_call_details):
        start = perf_counter()
        try:
            return continuation(handler_call_details)
        finally:
            duration = perf_counter() - start
            name = handler_call_details.method
            log.info(f"{name} took {duration: .3f}sec")

def main():
    port = config.PORT
    server = build_server(port, secure=True)

    # Start server
    server.start()
    log.info(f"Server ready on {port}")
    server.wait_for_termination()

# Run from Ch06 with: python3 server_main.py
#
# = = = = = = = = = =
#
# Request with HTTPS
# grpcurl --insecure -d @ localhost:8888 Rides.Start < request.json
#
#
#
#
#
#
#
#
#
#
#
#
