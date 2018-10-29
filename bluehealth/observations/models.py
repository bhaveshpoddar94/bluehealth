from django.db import models
# from bluehealth.devices.models import Device
# Create your models here.

ATTR = {
    'f1': ['Ambient Temperature', '\u00b0C', '#ff4d4d'],
    'f2': ['Ambient Pressure', 'hPa', '#7fff7f'],
    'f3': ['Water Temperature', '\u00b0C', '#66b2ff'],
    'f4': ['Water Depth', 'cm', '#ffc04d'],
    'f5': ['GPS Latitude', '\u00b0', '#D2691E'],
    'f6': ['GPS Longitude', '\u00b0', '#D2691E'],
    'f7': ['Altitude', 'm', '#9F00B3'],
    'f8': ['Luminosity', 'lux', '#FFD700'],
}


class Attribute(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=5)
    value = models.FloatField()

    def __str__(self):
        return '%s: %d' % (self.type, self.value)

    class Meta:
        ordering = ('created',)
