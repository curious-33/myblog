from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datetime import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']