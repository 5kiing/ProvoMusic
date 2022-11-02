from django.shortcuts import render
from django.http import HttpResponse

def eventsPageView(request) :
        return HttpResponse('This is the events page') 

# Create your views here.
