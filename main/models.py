from django.db import models

class AqiData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    aqi_25 = models.PositiveIntegerField()
    aqi_100 = models.PositiveIntegerField()


