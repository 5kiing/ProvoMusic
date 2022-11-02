from django.urls import path
from .views import eventsPageView

urlpatterns = [
    path("events/", eventsPageView, name="venue")    
] 