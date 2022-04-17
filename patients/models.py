import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self) -> str:
        return f"P:{self.patient} - Dr:{self.doctor} || {self.date} {self.time}"

class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
