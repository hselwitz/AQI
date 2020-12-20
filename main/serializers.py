from rest_framework import serializers
from main.models import AqiData


class AQISerializer(serializers.ModelSerializer):
    class Meta:
        model = AqiData
        fields = ('time', 'aqi_25', 'aqi_100')
