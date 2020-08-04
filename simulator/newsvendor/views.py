from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django import forms
from . import models

from .models import *


# Create your views here.
no_of_questions = question.objects.count()

def index(request):
    return render(request,"newsvendor/index.html")


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
        que = question.objects.get(qid = 1)
        q = {   
                'uid' : u.uid,
                'qid' : que.qid,
                'CO' : que.CO,
                'CU' : que.CU,
                'even' : que.even
        }
        return JsonResponse(q)


class roundSubmit(View):
    def get(self,request):
        uid = request.GET['uid']
        qid = int(request.GET['qid'])
        pf = request.GET['point_forecast']
        lb = request.GET['LB']
        ub = request.GET['UB']
        tf = request.GET['target_fill_rate']

        a = answer(
            uid = uid,
            qid = qid,
            point_forecast = pf,
            LB = lb,
            UB = ub,
            target_fill_rate = tf
            )
        a.save()

        if (qid+1) <= no_of_questions:
            newqid = qid+1
            que = question.objects.get(qid = newqid)
            q = {
            'qid': que.qid,
            'CO': que.CO,
            'CU': que.CU,
            'even': que.even
            }
            return JsonResponse(q)
        else:
            msg = 'Thank you for taking part in the survey'
            return HttpResponse(msg)
