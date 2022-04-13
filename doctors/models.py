from django.db import models

# Create your models here.


class Specializaion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    picture = models.ImageField(upload_to="media", null=True, blank=True)
    specialization = models.ForeignKey("Specializaion",related_name='doctors', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
