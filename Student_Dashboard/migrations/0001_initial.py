# Generated by Django 3.2.8 on 2021-11-25 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Exam_Dashboard', '0002_auto_20211125_1548'),
        ('Login_App', '0003_alter_studentmodel_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('negative_marking', models.DecimalField(decimal_places=2, max_digits=3)),
                ('timestamp', models.TimeField(auto_now_add=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_result', to='Exam_Dashboard.exammodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_result', to='Login_App.studentmodel')),
            ],
        ),
    ]