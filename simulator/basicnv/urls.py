from django.urls import path

from .views import *

app_name="basicnv"
urlpatterns=[
    path("",index,name="index")
]
