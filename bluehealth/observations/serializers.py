from rest_framework import serializers
from models import Attribute as Observation


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ['pk', 'obs_type', 'value']

    # converts to JSON
    # validation for data passed
