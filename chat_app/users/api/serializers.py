from django.contrib.auth import get_user_model
from rest_framework import serializers

from chat_app.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name"]
