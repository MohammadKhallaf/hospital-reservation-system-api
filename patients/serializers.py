from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from doctors.serializers import DoctorSerializer

import patients
from .models import Appointment, Patient

class PatientSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerliazer()
    class Meta:
        model = Appointment
        fields ='__all__'