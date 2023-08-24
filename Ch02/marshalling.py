""" Serialization and Deserialization of request """

import rides_pb2 as pb

request = pb.StartRequest(
    car_id = 95,
    driver_id = "McQueen",
    passenger_ids = ["p1", "p2", "p3"],
    type = pb.POOL,
    location = pb.Location(
        lat = 32.5270941,
        lng = 34.9404309
    )
)
print(request)

# Marshal (serialization)
data = request.SerializeToString()
print("type: ", type(data))
print("size: ", len(data))
print("\n==============================\n")

# Unmarshal (deserialization)
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)
print("\n==============================\n")

# prints True
print(request == request2)
