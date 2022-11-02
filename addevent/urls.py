from django.urls import path
from .views import addEventPageView

urlpatterns = [
    path("addEvent/", addEventPageView, name="venue")    
] 