# Generated by Django 4.0.4 on 2022-04-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_rename_specializaion_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]