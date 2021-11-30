from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from select import error
from django.contrib.auth.models import User
from .models import *


class Student_RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Reg
        fields = '__all__'


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "phone_number", "password",)


class Student_RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
