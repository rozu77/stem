# Generated by Django 3.0.2 on 2020-05-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0018_auto_20200524_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_info',
            name='date',
        ),
    ]