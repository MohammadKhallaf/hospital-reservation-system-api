from rest_framework import serializers

from .models import Appointment, Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_id = serializers.ReadOnlyField()
    patient_id = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = "__all__"
