from os import name
from django.urls import path
from django.http import HttpResponse

from . import views

def home(request):
    return HttpResponse("Home sweet home")

urlpatterns = [
    path('', home, name='home'),
]