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
        uid = u.uid
        rids = rounds.objects.values_list('roundid', flat=True)
        ac_demands = []
        for i in range(0,min(len(rids),15)):
            ac_demands.append(rounds.objects.get(roundid = rids[i]).actualdemand)
        q = {   
                'uid' : uid,
                'rid' : 15,
                'actualdemand' : ac_demands
        }
        return JsonResponse(q)


class roundSubmit(View):
    def get(self,request):
        uid = request.GET['uid']
        rid = int(request.GET['rid'])
        pf = request.GET['point_forecast']

        a = answer(
            uid = uid,
            roundid = rid,
            point_forecast = pf
            )
        a.save()
        new_round = rounds.objects.filter(roundid__gt = rid)[:1]
        if new_round:
            newrid = new_round[0].roundid
            newdemand = new_round[0].actualdemand
            q = {
            'uid' : uid,
            'rid' : newrid,
            'actualdemand' : newdemand
            }
            return JsonResponse(q)
        else:
            msg = 'Thank you for taking part in the survey'
            return HttpResponse(msg)