from rest_framework import generics, mixins
from .permissions import IsOwnerOrReadOnly
from ..models import Device
from .serializers import DeviceSerializer


class DeviceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'pk'
    permissions = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Device.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Device.objects.all()
