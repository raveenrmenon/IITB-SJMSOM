from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django import forms
from . import models

from .models import question,user,answer


# Create your views here.

def index(request):
    return render(request,"newsvendor/index.html",{
         "questions":question.objects.all()
     })

'''
def add(request):
    # form=NewTaskForm(request.POST)
    # if form.is_valid():
    #     email=form.cleaned_data["email"]
    #     email_id.append(email)
    # if email in email_id:
    #     return HttpResponseRedirect(reverse("newsvendor:index"))
    # else:
        
        return render(request,"newsvendor/description.html")

def round(request):
    return render(request,"newsvendor/round.html")
'''

class checkEmail(View):
    def get(self, request):
        email_id = request.GET['email']
        a = user.objects.filter(email=email_id).exists()
        return HttpResponse(a)


 
# def checkEmail(request):
#     email_id = request.GET['email']
#     a = user.objects.filter(email=email_id).exists()
#     return a


