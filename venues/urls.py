from django.urls import path
from .views import venuesPageView

urlpatterns = [
    path("venue/", venuesPageView, name="venue")    
]