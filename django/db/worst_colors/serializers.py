from rest_framework import serializers
from .models import WorstColor


class WorstColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorstColor
        fields = '__all__'
