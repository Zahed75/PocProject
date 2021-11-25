from django.db import models

from django.contrib.auth.models import User

from Exam_Dashboard.models import *
from Login_App.models import *

# Create your models here.


class ExamResult(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='student_result')
    exam_name = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='exam_result')
    score = models.DecimalField(max_digits=3, decimal_places=2)
    negative_marking = models.DecimalField(max_digits=3, decimal_places=2)
    timestamp = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.student.full_name + "-" + str(self.score)