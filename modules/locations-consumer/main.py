import os
from app.models import Location  # noqa
from app.services import LocationService
from kafka import KafkaConsumer

# Kafka consumer initialization
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER)

# Consumer startup. Every new message will be processed and saved to the database
print("Starting locations consumer...")
try:
    for message in consumer:
        print (message.value.decode('utf-8'))    
        location: Location = LocationService.create(message.value.decode('utf-8'))
except KeyboardInterrupt:
    print("Stopping locations consumer...")
    consumer.close()