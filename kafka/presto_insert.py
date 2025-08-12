from kafka import KafkaConsumer
from prestodb import dbapi
import json
import os

KAFKA_BROKER = os.environ.get('KAFKA_BROKER', 'kafka.kafka.svc.cluster.local:9092')
PRESTO_HOST = os.environ.get('PRESTO_HOST', 'presto.presto.svc.cluster.local')
print("Connecting to Kafka broker: ", KAFKA_BROKER)
print("Connecting to Presto: ", PRESTO_HOST)

# Connect to Kafka
consumer = KafkaConsumer(
    'opensky-topic-3',
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# Connect to Presto inside cluster
conn = dbapi.connect(
    host=PRESTO_HOST,
    port=8080,
    user='admin',
    catalog='iceberg',
    schema='default'
)
cursor = conn.cursor()
print(conn)

# Loop to read from Kafka and insert into Iceberg
for message in consumer:
    print("Message: ", message)
    data = message.value
    callsign = data["callsign"].replace("'", "''")
    country = data["origin_country"].replace("'", "''")
    insert_sql = f"""
    INSERT INTO flight_data (
        icao24, callsign, origin_country, time_position,
        longitude, latitude, velocity
    )
    VALUES (
        '{data["icao24"]}', '{callsign}', '{country}', {data["time_position"]},
        {data["longitude"]}, {data["latitude"]}, {data["velocity"]}
    )
    """
    try:
        cursor.execute(insert_sql)
        print("Inserted:", data["icao24"])
    except Exception as e:
        print("Error inserting:", e)