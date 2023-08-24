""" Unittest for server.py """

import unittest
from unittest.mock import MagicMock, patch

import grpc
import src.libraries.config as config
import src.server.rides_pb2 as pb
import src.server.rides_pb2_grpc as rpc

from datetime import datetime
from socket import socket
from src.client.client import Client, rand_events
from src.server.server import build_server, get_free_port

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.host = config.HOST
        self.port = get_free_port()
        self.address = f"{self.host}:{self.port}"
        self.server = build_server(self.port, secure=False)
        self.server.start()

    def tearDown(self):
        self.server.stop(grace=None)

    @patch("src.server.server.new_ride_id")
    def test_start_ride(self, mock_new_ride_id):
        mock_new_ride_id.return_value = "ABC123"

        client = Client(self.address)
        ride_id = client.start_ride(
            car_id=7,
            driver_id='Bond',
            passenger_ids=['M', 'Q'],
            type='POOL',
            lat=51.4871871,
            lng=-0.1266743,
            time=datetime(2021, 9, 30, 20, 15)
        )

        self.assertEqual(ride_id, "ABC123")

    def test_track(self):
        events = rand_events(2)

        client = Client(self.address)
        response = client.track(events)

        self.assertEqual(response.count, 2)

if __name__ == "__main__":
    # To run:
    # 1. export PYTHONPATH=<path-to-project>/python_grpc/Ch06/
    # 2. cd to 'test' folder
    # 3. python3 -m unittest server/test_server.py
    unittest.main()
