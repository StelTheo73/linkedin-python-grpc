""" Handle enum types """

import rides_pb2 as pb

# Prints 0
print(pb.REGULAR)
# Prints 1
print(pb.POOL)
# Prints REGULAR
print(pb.RideType.Name(pb.REGULAR))
# Prints POOL
print(pb.RideType.Name(pb.POOL))
# Prints 0
print(pb.RideType.Value("REGULAR"))
# Prints 1
print(pb.RideType.Value("POOL"))
