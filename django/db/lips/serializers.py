from rest_framework import serializers
from .models import Lip


class LipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lip
        fields = '__all__'
