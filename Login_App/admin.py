from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone_number', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'active', 'staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2')}
         ),
    )
    search_fields = ['phone_number']
    ordering = ['phone_number']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'full_name', 'batch', 'institution',)


@admin.register(ExamTool)
class ExamToolModelAdmin(admin.ModelAdmin):
    list_display = ('level', 'batch', 'board')


# @admin.register(Student_Reg)
# class Student_RegModelAdmin(admin.ModelAdmin):
#     list_display = ['__all__']


@admin.register(Student_Profile)
class Student_ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','level','batch','board','institution')


@admin.register(Student_Reg)
class Student_Reg(admin.ModelAdmin):
    list_display = ('id','phone_number')
