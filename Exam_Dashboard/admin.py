from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Batch)
class BatchModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ExamPack)
class ExamPackModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','details','batch')


@admin.register(ExamModel)
class ExamModelModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','details','time',
                    'date','batch','exam_pack','total_mark','pass_mark','amount_per_mistake')




@admin.register(ExamUtils)
class ExamUtilsModelAdmin(admin.ModelAdmin):
    list_display = ('level','batch')