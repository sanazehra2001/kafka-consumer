from django.urls import path
from . import views

urlpatterns = [
    path('consume/<str:topic>/', views.consume_kafka_messages, name='consume_kafka_messages'),
]
