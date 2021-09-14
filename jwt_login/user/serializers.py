from user.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()


class IndexSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields ='__all__'