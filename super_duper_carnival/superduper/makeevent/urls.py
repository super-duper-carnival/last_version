from django.conf.urls import url
from django.urls import path
from .views import make

urlpatterns =  [
    path('makeevent/', make),
]
