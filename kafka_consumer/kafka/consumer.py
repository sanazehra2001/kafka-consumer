import sys
from kafka import KafkaConsumer

import json

from django.apps import apps

import os
import django

# Initialize Django
django.setup()


def get_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=['kafka:9093'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest'
    )

# def insert_task_to_db(title, description, due_date, is_completed, priority, category, user):
#     try:
#         Task = apps.get_model('kafka_consumer', 'Task')
#         Task.objects.create(
#             title=title,
#             description=description,
#             due_date=due_date,
#             is_completed=is_completed,
#             priority=priority,
#             category=category,
#             user=user
#         )
#         print("Task inserted into database.")
#     except Exception as e:
#         print(f"Error inserting task into database: {e}")


# def consume_messages(topic):
#     print("Called")
#     consumer = get_consumer(topic)
#     print(consumer)

#     for message in consumer:
#         print(message)
#         try:
#             if not message.value:  # Check if the message is empty
#                 print("Received empty message")
#                 continue
            
#             if not isinstance(message.value, dict):
#                 print(f"Unexpected message format: {message.value}")
#                 continue
            
#             # Process the message
#             task = message.value.get('task_data')
#             user = message.value.get('user_data')
            
#             if task is None:
#                 print(f"Received incomplete message: {message.value}")
#                 continue

#             print(f"Received Task: {task}")

#             if user is None:
#                 print(f"User information is missing: {message.value}")
#                 continue

#             print(f"Task created by: {user}")

#             title = task['title']
#             description = task.get('description', '')  # Default to empty string if not provided
#             due_date = task.get('due_date')
#             is_completed = task.get('is_completed', False)  # Default to False if not provided
#             priority = task.get('priority', 'medium')  # Default to 'medium' if not provided
#             category = task.get('category')
#             user = user

#             insert_task_to_db(title, description, due_date, is_completed, priority, category, user)
        
#         except json.JSONDecodeError as e:
#             print(f"Error decoding message: {e}")
#             print(f"Raw message: {message.value}")





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: consumer.py task_topic")
        sys.exit(1)
    
    topic = sys.argv[1]
    # consume_messages(topic)