# Generated by Django 3.0.2 on 2020-05-24 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0015_auto_20200524_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
