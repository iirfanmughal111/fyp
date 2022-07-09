from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator
# Create your models here.


class devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    vehicle_no = models.IntegerField( validators=[MaxValueValidator(9999), MinValueValidator(0)])
    route_name = models.CharField(max_length=70)
    temperature = models.BooleanField(default=False)
    carbon_mono = models.BooleanField(default=False)
    humidity = models.BooleanField(default=False)
    light = models.BooleanField(default=False)
    noise = models.BooleanField(default=False)
    langitude = models.BooleanField(default=False)
    latitude = models.BooleanField(default=False)
    def __str__(self):
        return self.route_name



class sensors(models.Model):
    sensor_id = models.ForeignKey(devices,on_delete=models.CASCADE)
    temperature = models.FloatField()
    carbon_mono = models.FloatField()
    humidity = models.FloatField()
    light = models.FloatField()
    noise = models.FloatField()
    langitude = models.FloatField()
    latitude = models.FloatField()



