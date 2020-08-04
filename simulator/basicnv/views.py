from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django import forms
from . import models

from .models import *
# Create your views here.


def index(request):
    return render(request,"basicnv/index.html")

class checkEmail(View):
    def get(self, request):
        email_id = request.GET['email']
        a = user.objects.filter(email=email_id).exists()
        return HttpResponse(a)

class userSubmit(View):
    def get(self, request):
        uemail = request.GET['email']
        uname = request.GET['name']
        ugender = request.GET['gender']
        uage = request.GET['age']
        uorganisation = request.GET['organisation']
        udesignation = request.GET['designation']

        u = user(
            name = uname,
            email = uemail,
            gender = ugender,
            age = uage,
            organisation = uorganisation,
            designation = udesignation
            )
        u.save()
        # que = question.objects.get(qid = 1)
        q = {   
                'uid' : u.uid,
                # 'qid' : que.qid,
                # 'CO' : que.CO,
                # 'CU' : que.CU,
                # 'even' : que.even
        }
        return JsonResponse(q)
