from django.contrib import admin
from .models import Device
# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Device, DeviceAdmin)
