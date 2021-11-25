from os import name
from django.urls import path
from django.http import HttpResponse

from . import views

app_name = 'Student_Dashboard'

def student(request):
    return HttpResponse("Home sweet home")

urlpatterns = [
    path('student/', student, name='student'),
]