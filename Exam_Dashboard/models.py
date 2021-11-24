from django.db import models

from django.contrib.auth.models import User
from Login_App.models import *


# Create your models here.

class Batch(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Batch')

    def __str__(self):
        return self.name


class ExamPack(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Exam Pack Name')
    details = models.TextField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='exam_pack_batch')
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
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='exam_batch')
    exam_pack = models.ForeignKey(ExamPack, on_delete=models.CASCADE, related_name='exam_pack')

    # marking
    total_mark = models.IntegerField(default=0)
    pass_mark = models.IntegerField(default=0)

    isRandomized = models.BooleanField(default=False, verbose_name='Randomization')
    isSorted = models.BooleanField(default=False, verbose_name='Sorting')

    # for negative marking
    isNegativeMarking = models.BooleanField(default=False, verbose_name='Negative Marking')
    amount_per_mistake = models.IntegerField(default=0, verbose_name='Amount per mistake')

    def __str__(self):
        return self.name


class QuestionModel(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    question_body=models.TextField(max_length=1000)
    question_img=models.ImageField(upload_to='question_bank')
    ans=(
        ''
    )
