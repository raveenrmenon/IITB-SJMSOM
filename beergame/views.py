from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.urls import reverse
from django import forms
from . import models
# Create your views here.

def index(request):
	return HttpResponse("Hello world! Beergame here")
