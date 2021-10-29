import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

# channel = grpc.insecure_channel("udaconnect-kafka:5005")
channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    person_id=2,
    latitude='-122.290883',
    longitude='37.55363',
    created_at='2020-08-15T10:37:06'
)

response = stub.Create(location)
