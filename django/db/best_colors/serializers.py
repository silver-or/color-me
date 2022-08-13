from rest_framework import serializers
from .models import BestColor


class BestColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestColor
        fields = '__all__'
