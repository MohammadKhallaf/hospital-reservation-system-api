from rest_framework import serializers
from .models import Doctor, Schedule, Specialization


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
