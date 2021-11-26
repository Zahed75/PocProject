from django.db import models

# from django.contrib.auth.models import User
from Login_App.models import *


# Create your models here.


class ExamPack(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Exam Pack Name')
    details = models.TextField()
    batch = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='exam_pack_cover_photos', null=True, blank=True)

    def __str__(self):
        return self.name


class ExamModel(models.Model):
    name = models.CharField(max_length=1000)
    details = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    cover_photo = models.ImageField(upload_to='exam_cover_photos', blank=True, null=True)

    # assign student
    level = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE, related_name='exam_pack')

    # marking
    total_mark = models.IntegerField(default=0)
    pass_mark = models.IntegerField(default=0)
    mark_per_question = models.IntegerField(default=1)

    isRandomized = models.BooleanField(default=False, verbose_name='Randomization')
    isSorted = models.BooleanField(default=False, verbose_name='Sorting')

    # for negative marking
    isNegativeMarking = models.BooleanField(default=False, verbose_name='Negative Marking')
    amount_per_mistake = models.IntegerField(default=0, verbose_name='Amount per mistake')

    def __str__(self):
        return self.name


class Quiz(models.Model):

    # for quiz types
    type_choices = [
        ('type 1', 'type 1'),
        ('type 2', 'type 2'),
        ('type 3', 'type 3'),
    ]

    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    question_body = models.TextField(max_length=1000)
    paragraph = models.TextField(blank=True, null=True)
    question_img = models.ImageField(upload_to='question_bank', blank=True, null=True)
    exam_type = models.CharField(choices=type_choices, max_length=30)
    op_1 = models.CharField(max_length=200, null=True)
    op_2 = models.CharField(max_length=200, null=True)
    op_3 = models.CharField(max_length=200, null=True)
    op_4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.question_body




class ExamUtils(models.Model):
    level = models.CharField(max_length=100, blank=True)
    batch = models.CharField(max_length=100, blank=True)
    board = models.CharField(max_length=100,blank=True)