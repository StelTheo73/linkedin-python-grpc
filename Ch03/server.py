""" Simple grpc server 
Run from Ch03 folder with python3 server.py
"""

from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
from uuid import uuid4
from libraries.validate import InvalidFieldError

import grpc

import libraries.config as config
import libraries.log as log
import rides_pb2 as pb
import rides_pb2_grpc as rpc

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

    @staticmethod
    def validate_request(request):
        if not request.driver_id:
            raise InvalidFieldError("driver_id", "empty")
        # TODO (steltheo73): Validate more fields

if __name__ == "__main__":
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

# Run with: python3 server.py
#
# = = = = = = = = = =
# grpcurl --plaintext localhost:8888 list --> Returns the names that passed to reflection
#   Rides
#   grpc.reflection.v1alpha.ServerReflection
#
# = = = = = = = = = =
#
# grpcurl --plaintext localhost:8888 list Rides     --> returns the methods and the types of Rides
# grpcurl --plaintext localhost:8888 describe Rides --> describes Rides
# 
# = = = = = = = = = =
# 
# grpcurl --plaintext localhost:8888 describe .StartRequest --> returns the protocol buffer 
#                                                               definition of StartRequest
#
# = = = = = = = = = =
# Send request
#
# grpcurl --plaintext -d @ localhost:8888 Rides.Start < request.json
#   * -d: data
#   * @: read data from stdin
#   The StartResponse message is returned (as described from rides.proto),
#   showing the id of the generated ride_id
#   The server logs the request (what is included in the json file)
#
