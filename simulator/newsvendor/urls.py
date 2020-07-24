from django.urls import path

from . import views

app_name="newsvendor"
urlpatterns=[
    path("",views.index,name="index"),
]