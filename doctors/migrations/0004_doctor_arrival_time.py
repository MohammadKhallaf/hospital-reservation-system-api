# Generated by Django 4.0.4 on 2022-04-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_doctor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='arrival_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
