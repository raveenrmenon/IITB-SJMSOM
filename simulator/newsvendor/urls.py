from django.urls import path

from .views import *

app_name="newsvendor"
urlpatterns=[
    path("",index,name="index"),
    path("checkEmail",checkEmail.as_view()),
]