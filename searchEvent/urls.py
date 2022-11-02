from django.urls import path
from .views import searchEventPageView

urlpatterns = [
    path("searchEvent/", searchEventPageView, name="venue")    
] 