from rest_framework import serializers

from patients.serializers import PatientSerializer
from .models import Doctor, Schedule, Specialization
from patients.models import Appointment


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer()
    doctor_schedules = ScheduleSerializer(many=True)
    
    class Meta:
        model = Doctor
        fields = "__all__"



class DoctorAppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    class Meta:
        model = Appointment
        fields = "__all__"
