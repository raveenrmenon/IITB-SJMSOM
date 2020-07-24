from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import question,user,answer


# Create your views here.

def index(request):
     return render(request,"newsvendor/index.html",{
         "questions":question.objects.all()
     })



# def add(request):
#     if request.method=="POST":
#         if request.POST.get('email'):
#             saveEmail=user()
#             saveEmail.email=request.POST.get('email')
#             saveEmail.save()
#             return render(request,"newsvendor/description.html")
#         else:
#             return httpResponseRedirect(reverse('index'))

# def round(request):
    

#     return render(request,"newsvendor/round.html")