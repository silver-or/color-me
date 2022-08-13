from rest_framework import serializers
from .models import Hair


class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = '__all__'
