from rest_framework import serializers
from ..models import Attribute as Observation


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = [
            'pk',
            'created_at',
            'collected_at',
            'obs_type',
            'value'
        ]

    # converts to JSON
    # validation for data passed
