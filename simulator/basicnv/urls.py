from django.urls import path

from .views import *

app_name="basicnv"
urlpatterns=[
    path("",index,name="index"),
    path("emailAuth",emailAuth.as_view()),
    path("userRegister",userRegister.as_view()),
    path("roundData",roundData.as_view())
]
