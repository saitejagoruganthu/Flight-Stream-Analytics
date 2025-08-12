from kafka import KafkaProducer
import json
import requests
import time
import os
# Get Kafka broker from environment variable or use default
KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'kafka.kafka.svc.cluster.local:9092')
print("Connecting to Kafka broker:", KAFKA_BROKER)
# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
# OpenSky API endpoint
url = "https://opensky-network.org/api/states/all"
# Limit to 10 API calls total
for i in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        count = 0
        for state in data.get("states", []):
            if count >= 100:
                break
            message = {
                "icao24": state[0],
                "callsign": state[1] or "",
                "origin_country": state[2],
                "time_position": state[3],
                "longitude": state[5],
                "latitude": state[6],
                "velocity": state[9]
            }
            producer.send("opensky-topic-3", message)
            print(f"{count}: Sent:", message)
            count += 1
    else:
        print(f"API call failed with status code {response.status_code}")
    print(f"Waiting 30 seconds before next API call ({i+1}/10)...")
    time.sleep(30)
print("Done! Sent 1000 messages in 10 API calls.")

# from kafka import KafkaProducer
# import json
# import requests
# import time
# import os

# KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'kafka.kafka.svc.cluster.local:9092')
# print("Connecting to Kafka broker: ", KAFKA_BROKER)

# # Connect to Kafka
# producer = KafkaProducer(
#     bootstrap_servers=KAFKA_BROKER,
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# url = "https://opensky-network.org/api/states/all"

# # Infinite loop to fetch and publish data
# while True:
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         for state in data.get("states", []):
#             message = {
#                 "icao24": state[0],
#                 "callsign": state[1] or "",
#                 "origin_country": state[2],
#                 "time_position": state[3],
#                 "longitude": state[5],
#                 "latitude": state[6],
#                 "velocity": state[9]
#             }
#             producer.send("opensky-topic", message)
#             print("Sent:", message)
#     time.sleep(30)