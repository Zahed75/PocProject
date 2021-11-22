from os import name
from django.urls import path
from django.http import HttpResponse

from . import views

def dashboard(request):
    return HttpResponse("Home sweet home")

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]