# serializer는 JSON으로 변환한다.

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']