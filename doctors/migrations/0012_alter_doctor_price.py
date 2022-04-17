# Generated by Django 4.0.4 on 2022-04-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0011_alter_doctor_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]