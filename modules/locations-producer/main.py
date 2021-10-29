import json
import time
import os
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer

# Set up a Kafka producer
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "created_at": request.created_at,
        }

        kafka_data = json.dumps(request_value).encode()
        producer.send(TOPIC_NAME, kafka_data)
        producer.flush()

        print(request_value)

        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
