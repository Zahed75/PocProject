from django.db import models

from django.contrib.auth.models import User
from Login_App.models import *

# Create your models here.

class ExamModel(models.Model):
    name = models.CharField(max_length=1000)
    details = models.TextField()
    # time = models.TimeField()
    # date = models.DateField()
    cover_photo = models.ImageField(upload_to='exam_cover_photos', blank=True, null=True)
    
    # assign student
    # batch = models.ForeignKey()
    # exam_pack = models.ForeignKey()

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