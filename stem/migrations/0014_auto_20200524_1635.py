# Generated by Django 3.0.2 on 2020-05-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0013_student_info_d1_walking'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='d1_family_owned_vehicle',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student_info',
            name='d1_public_commute_landwater',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student_info',
            name='d1_school_service',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
