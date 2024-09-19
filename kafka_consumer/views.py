from django.http import JsonResponse
from django.shortcuts import render

from kafka_consumer.kafka.consumer import get_consumer
from .models import Task
import json

# Create your views here.
def consume_kafka_messages(request, topic):
    try:
        print("Called")
        # Initialize Kafka consumer for the specified topic
        consumer = get_consumer(topic)
        
        # Loop through the messages in the topic
        for message in consumer:
            try:
                if not message.value:  # Check if the message is empty
                    print("Received empty message")
                    continue

                if not isinstance(message.value, dict):  # Validate message format
                    print(f"Unexpected message format: {message.value}")
                    continue

                # Extract task and user data from the message
                task = message.value.get('task_data')
                user = message.value.get('user_data')

                print(task)
                print(user)

                if task is None:
                    print(f"Received incomplete message: {message.value}")
                    continue

                # Extract individual task fields
                title = task.get('title')
                description = task.get('description', '')
                due_date = task.get('due_date')
                is_completed = task.get('is_completed', False)
                priority = task.get('priority', 'medium')
                category = task.get('category')
                user_email = user  

                Task.objects.create(
                    title=title,
                    description=description,
                    due_date=due_date,
                    is_completed=is_completed,
                    priority=priority,
                    category=category,
                    user=user
                )

            except json.JSONDecodeError as e:
                print(f"Error decoding message: {e}")
                continue

        return JsonResponse({"status": "Messages consumed successfully"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)