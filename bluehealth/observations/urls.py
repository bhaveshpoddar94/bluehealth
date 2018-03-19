from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name="Home"),
    url(r'^save-values/', views.save_attr, name="Save Values"),
    url(r'^analytics/', views.analytics, name="Analytics"),
    url(r'^list-latest/', views.list_latest, name="List Latest"),
    # url(r'^ajax-hour-data/', views.ajax_hour_data, name="Ajax Hour Data"),
    url(r'^ajax-data/', views.ajax_data, name="Ajax Data"),
    url(r'^ajax-add-data/', views.ajax_add_data, name="Ajax Add Data"),
    url(r'^ajax-com-data/', views.ajax_com_data, name="Ajax Comparison Data"),
    url(r'^analytics-com/', views.analytics_com, name="Analytics Comparison"),
]
