from os import name
from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'PocApp'

def poc(request):
    return HttpResponse("Home sweet home")

urlpatterns = [
    path('poc/', poc, name='home'),
]