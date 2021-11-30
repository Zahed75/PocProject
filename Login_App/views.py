from django.shortcuts import render, HttpResponseRedirect, redirect
# from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics


class Register(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = Student_RegSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': "something went wrong"})

        serializer.save()

        user = User.objects.get(phone_number=serializer.data['phone_number'])
        refresh = RefreshToken.for_user(user)
        return Response(
            {'status': 202, 'payload': serializer.data, 'refresh': str(refresh),
             'access': str(refresh.access_token), 'message': "your data was saved"})


