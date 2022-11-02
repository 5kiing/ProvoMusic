from django.shortcuts import render
from django.http import HttpResponse

def landingPageView(request) :
        return HttpResponse('This is the landing page') 

# Create your views here.
