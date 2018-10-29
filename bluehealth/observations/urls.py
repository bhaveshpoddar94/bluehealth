from django.conf.urls import url
from .views import (ObservationRetrieveUpdateDestroyAPIView,
                    ObservationAPIView)

urlpatterns = [
    url(
        r'^$',
        ObservationAPIView.as_view(),
        name='device-listcreate'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        ObservationRetrieveUpdateDestroyAPIView.as_view(),
        name='device-rud'
    ),

]
