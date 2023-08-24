""" Simple grpc server 
Run from Ch05 folder with python3 server_main.py
"""

from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
from uuid import uuid4
from libraries.validate import InvalidFieldError

import grpc
import libraries.config as config
import libraries.log as log
import server.rides_pb2 as pb
import server.rides_pb2_grpc as rpc

def new_ride_id() -> str:
    """ Returns a random UUID in hex format. """
    return uuid4().hex

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

def main():
    # Create generic grpc server (our server)
    server = grpc.server(ThreadPoolExecutor())
    # Register our server inside grpc server (from rpc module)
    rpc.add_RidesServicer_to_server(Rides(), server)

    # Reflection: external clients can query the server
    # about the available methods and types
    names = (
        pb.DESCRIPTOR.services_by_name["Rides"].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(names, server)

    address = f"[::]:{config.PORT}"
    # Force grpc to NOT use HTTPS
    server.add_insecure_port(address)

    # Start server
    server.start()
    log.info(f"Server ready on {address}")
    server.wait_for_termination()

# Run from Ch05 with: python3 server_main.py
#
# = = = = = = = = = =
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
#
#
