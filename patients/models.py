from enum import unique
import django
from django.db import models


# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self) -> str:
        return f"P:{self.patient} - D:{self.doctor}"

class Patient(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
