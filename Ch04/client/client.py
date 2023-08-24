""" Simple grpc client
Run from Ch04 folder with python3 client_main.py
"""

from client.exceptions import ClientError
from datetime import datetime

import grpc
import libraries.config as config
import libraries.log as log
import server.rides_pb2 as pb
import server.rides_pb2_grpc as rpc

class Client:
    """ Simple grpc client """

    def __init__(self, address) -> None:
        self.channel = grpc.insecure_channel(address)
        self.stub = rpc.RidesStub(self.channel)
        log.info(f"connected to {address}")

    def start_ride(self, car_id, driver_id, passenger_ids, type, lat, lng, time):
        """ Creates and starts a 'Rides' request """
        request = pb.StartRequest(
            car_id=car_id,
            driver_id=driver_id,
            passenger_ids=passenger_ids,
            type=pb.POOL if type == 'POOL' else pb.REGULAR,
            location=pb.Location(lat=lat, lng=lng)
        )
        request.time.FromDatetime(time)
        log.info(f"ride created: {request}")

        # Call Start method of grpc server
        try:
            response = self.stub.Start(request)
        except  grpc.RpcError as err:
            log.error(f"start: {err} ({err.__class__.__mro__})")
            raise ClientError(err.code, err.details) from err

        log.info(f"ride started with id: {response}")
        return response.id

    def close(self):
        """ Close connection with server """
        self.channel.close()

def main():
    """ Creates a client and starts a ride """
    address = f"{config.HOST}:{config.PORT}"
    client = Client(address)
    try:
        ride_id = client.start_ride(
            car_id=7,
            driver_id='Bond',
            passenger_ids=['M', 'Q'],
            type='POOL',
            lat=51.4871871,
            lng=-0.1266743,
            time=datetime(2021, 9, 30, 20, 15),
        )
        log.info(f"ride id: {ride_id}")
    except ClientError as err:
        log.error(f"client error occurred: {err.code}")

# Run from Ch04 with: python3 client_main.py
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
