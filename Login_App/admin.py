from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'full_name', 'batch', 'institution', 'board')
