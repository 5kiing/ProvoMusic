from django.urls import path
from .views import editEventPageView

urlpatterns = [
    path("editEvent/", editEventPageView, name="venue")    
] 