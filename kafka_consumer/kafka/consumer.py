import sys
from kafka import KafkaConsumer
import json
import django

# Initialize Django
django.setup()


def get_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=['kafka:9093'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        group_id='consumer_group_1'
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: consumer.py task_topic")
        sys.exit(1)
    
    topic = sys.argv[1]
