from django.db import models
from django.contrib.auth.models import User

from Exam_Dashboard.models import Batch

# Create your models here.

class StudentModel(models.Model):

    boards = [
        ('Dhaka', 'Dhaka'),
        ('Rajshahi', 'Rajshahi'),
        ('Comilla', 'Comilla'),
        ('Jessore', 'Jessore'),
        ('Chittagong', 'Chittagong'),
        ('Barisal', 'Barisal'),
        ('Sylhet', 'Sylhet'),
        ('Dinajpur', 'Dinajpur'),
        ('Madrasah', 'Madrasah'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_auth')
    phone_number = models.CharField(max_length=14, unique=True, verbose_name='Phone number')
    full_name = models.CharField(max_length=100, blank=False, verbose_name='Full Name')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='student_batch')
    institution = models.CharField(max_length=500)
    board = models.CharField(choices=boards, max_length=100)
    
    # otp 
    
    def __str__(self):
        return self.user.username + " " + self.phone_number

