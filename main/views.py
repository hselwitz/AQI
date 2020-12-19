from django.shortcuts import render

from main.models import AqiData


def index(request):
    aqi_last = AqiData.objects.last()
    ctx = {"aqi_last_25": aqi_last.aqi_25, "aqi_last_time": aqi_last.time}

    return render(request, 'main/index.html', ctx)
