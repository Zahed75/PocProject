from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.contrib.auth.models import User

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone_number:
            raise ValueError('Users must have an valid phone number')

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone_number, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_number = models.CharField(
        verbose_name='Phone Number',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.phone_number

    def get_short_name(self):
        # The user is identified by their email address
        return self.phone_number

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        return self.active


class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_auth')
    phone_number = models.CharField(max_length=14, unique=True, verbose_name='Phone number')
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Full Name')
    batch = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=500, blank=True, null=True)
    board = models.CharField(max_length=50, blank=True, null=True)

    # otp 

    def __str__(self):
        return self.user.username + " " + self.phone_number


class Student_Reg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=11,default='01')

    def __str__(self):
        return self.phone_number

class Student_Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False,verbose_name='Student Name')
    email=models.EmailField(max_length=22,blank=True,null=True,verbose_name='Student Mail')
    level=models.CharField(max_length=30,blank=False,verbose_name='Student level')
    batch=models.CharField(max_length=40,blank=False,verbose_name='Studnt Batch')
    board=models.CharField(max_length=300,blank=False,verbose_name='Student Board')
    institution=models.CharField(max_length=100,blank=False,verbose_name='Student Instituton')

    def __str__(self):
        return self.name


class ExamTool(models.Model):
    level = models.CharField(max_length=100, blank=True)
    batch = models.CharField(max_length=100, blank=True)
    board = models.CharField(max_length=100,blank=True)