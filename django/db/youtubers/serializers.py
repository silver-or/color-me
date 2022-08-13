from rest_framework import serializers
from .models import Youtuber


class YoutuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtuber
        fields = '__all__'
