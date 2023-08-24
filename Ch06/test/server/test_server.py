""" Unittest for server.py """

import unittest
from unittest.mock import MagicMock, patch

import src.server.rides_pb2 as pb
import src.server.rides_pb2_grpc as rpc

from datetime import datetime
from socket import socket
from src.server.server import Rides

class RidesTest(unittest.TestCase):

    @patch("src.server.server.new_ride_id")
    def test_start(self, mock_new_ride_id):
        request = pb.StartRequest(
            car_id=7,
            driver_id='Bond',
            passenger_ids=['M', 'Q'],
            type=pb.POOL,
            location=pb.Location(
                lat=51.4871871,
                lng=-0.1266743,
            )
        )

        context = MagicMock()
        mock_new_ride_id.return_value = "ABC123"

        rides = Rides()
        response = rides.Start(request, context)

        self.assertEqual(response.id, "ABC123")

    @patch("src.server.server.uuid4")
    def test_start_2(self, mock_uuid4):
        """ Same as test_start, just an alternative way to patch uuid4 """

        request = pb.StartRequest(
            car_id=7,
            driver_id='Bond',
            passenger_ids=['M', 'Q'],
            type=pb.POOL,
            location=pb.Location(
                lat=51.4871871,
                lng=-0.1266743,
            )
        )

        context = MagicMock()
        mock_uuid4().hex = "ABC123"

        rides = Rides()
        response = rides.Start(request, context)

        self.assertEqual(response.id, "ABC123")

if __name__ == "__main__":
    # To run:
    # 1. export PYTHONPATH=<path-to-project>/python_grpc/Ch06/
    # 2. cd to 'test' folder
    # 3. python3 -m unittest server/test_server.py
    unittest.main()
