from django.db import models
# from bluehealth.devices.models import Device
# Create your models here.


class Attribute(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    collected_at = models.DateTimeField(null=True, blank=True)
    obs_type = models.CharField(max_length=2)
    value = models.FloatField()
