# Generated by Django 4.0.4 on 2022-04-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]