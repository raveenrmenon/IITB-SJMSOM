from django.urls import path

from . import views

app_name="newsvendor"
urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("round",views.round,name="round")
]