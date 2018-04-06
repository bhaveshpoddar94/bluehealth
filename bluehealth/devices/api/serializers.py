from rest_framework import serializers
from ..models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'pk',
            'name',
            'location_address',
            'uuid',
            'manufacturer_id'
        ]

    # converts to JSON
    # validation for data passed
