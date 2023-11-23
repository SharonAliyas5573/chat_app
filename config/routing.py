from django.urls import path
 
from chat_app.chats.consumer import ChatConsumer
 
websocket_urlpatterns = [path("", ChatConsumer.as_asgi())]