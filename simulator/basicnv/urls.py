from django.urls import path

from .views import *

app_name="basicnv"
urlpatterns=[
    path("",index,name="index"),
    path("checkEmail",checkEmail.as_view()),
    path("userSubmit",userSubmit.as_view()),
    path("roundSubmit",roundSubmit.as_view())
]
