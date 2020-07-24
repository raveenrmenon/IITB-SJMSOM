from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from . import models

email_id=[]

class NewTaskForm(forms.Form):
    email=forms.EmailField(label="Enter your Email-Id:")

# Create your views here.

def index(request):
    return render(request,"newsvendor/index.html")

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


def validateEmail(request):
    email_id = request.GET['email']
    try:
        a = user.objects.get(email=email_id)
    except:
        a = None

    if a:
        HttpResponse('Success')
    else:
        HttpResponse("Failure")