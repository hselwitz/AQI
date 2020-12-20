import time
from math import floor

from django.shortcuts import render
from rest_framework import generics

from main.models import AqiData
from main.serializers import AQISerializer


def time_since_last(aqi_last_time):
    time_ago = floor((time.time() - aqi_last_time.timestamp()) / 60)
    if time_ago == 0:
        text = 'now'
    elif time_ago == 1:
        text = "1 minute ago"
    else:
        text = str(time_ago) + " minutes ago"

    return text


class AQICreate(generics.ListCreateAPIView):
    queryset = AqiData.objects.all()
    serializer_class = AQISerializer


def index(request):
    aqi_last = AqiData.objects.last()
    ctx = {"aqi_last_25": aqi_last.aqi_25,
           "aqi_last_time": time_since_last(aqi_last.time)}

    return render(request, 'main/index.html', ctx)
