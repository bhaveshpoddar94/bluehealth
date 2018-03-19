from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated
from ..models import Device
from .serializers import DeviceSerializer


class FlavorListCreateAPIView(ListCreateAPIView):
    queryset = Device.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceSerializer
    lookup_field = 'uuid' # Don't use Flavor.id!

class FlavorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceSerializer
    lookup_field = 'uuid' # Don't use Flavor.id!
