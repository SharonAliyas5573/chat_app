from django.urls import path

from chat_app.chats.consumer import NotificationConsumer, ChatConsumer

websocket_urlpatterns = [
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/", NotificationConsumer.as_asgi()),
]
