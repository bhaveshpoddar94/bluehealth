from rest_framework import generics, mixins
from .permissions import IsOwnerOrReadOnly
from ..models import Attribute as Observation
from .serializers import ObservationSerializer


class ObservationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # queryset = Device.objects.all()
    serializer_class = ObservationSerializer
    lookup_field = 'pk'
    permissions = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Observation.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ObservationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    serializer_class = ObservationSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Observation.objects.all()
