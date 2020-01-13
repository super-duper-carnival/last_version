from django.conf.urls import url
from django.urls import path
from .views import view_events

urlpatterns =  [
    path('', view_events),
]
