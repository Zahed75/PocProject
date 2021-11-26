from typing_extensions import Required
from django.shortcuts import render, HttpResponseRedirect, redirect

from django.contrib.auth.models import User
from .models import *

from django.urls import reverse

# Create your views here.


def register(request):

    if request.method == "POST":
        full_name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        level = request.POST.get('level')
        batch = request.POST.get('batch')
        board = request.POST.get('board')
        institution = request.POST.get('institution')

        user = User(username='',email=email)
        user.set_password(password)
        user.save()

        student_obj = StudentModel(
            user = user,
            phone_number = phone_number,
            batch = batch,
            level = level,
            board = board,
            institution = institution,
        )
        student_obj.save()

        return redirect('/home/')


    context = {}
    template_name = 'register.html'
    return render(request, template_name, context)