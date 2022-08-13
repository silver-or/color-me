from rest_framework import serializers
from .models import PersonalColor


class PersonalColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalColor
        fields = '__all__'
