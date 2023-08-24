""" Handle date & time """

from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import rides_pb2 as pb

now = Timestamp()
now.GetCurrentTime()
# Current time in seconds and nanos
print(now)

print("\n==============================\n")

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3'],
    type=pb.POOL,
    location=pb.Location(
        lat=32.5270941,
        lng=34.9404309,
    )
)

print("\n==============================\n")

time = datetime(2022, 2, 13, 14, 39, 42)
# Convert from python datetime to protobuf time
# request.time = time --> this gives AttributeError
request.time.FromDatetime(time)
print(time)
print(request.time)

# Prints true
print(time == request.time.ToDatetime())

print("\n==============================\n")

print(request)
