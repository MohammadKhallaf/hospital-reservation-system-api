from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import doctors
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from patients.models import Appointment
from patients.serializers import AppointmentSerializer

"""
Doctors APP ENDPOINT
"""

@api_view(["GET"])
def get_all_doctors(request):
    doctor = Doctor.objects.all()
    doctor_serializer = DoctorSerializer(doctor, many=True)
    return Response(doctor_serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_new_doctor(request):
    doctor_serializer = DoctorSerializer(data=request.data)
    if doctor_serializer.is_valid():
        doctor_serializer.save()
        return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)
    return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor_serializer = DoctorSerializer(instance=doctor, data=request.data)
    if doctor_serializer.is_valid():
        doctor_serializer.save()
        return Response(doctor_serializer.data, status=status.HTTP_200_OK)
    return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return Response("deleted successfully")

"""
Doctor Appointments
"""

@api_view(["GET"])
def get_doctor_appointments(request,pk):
    doctor = Doctor.objects.get(id=pk)
    doctor_appointments = Appointment.objects.filter(doctor=doctor)
    doctor_appointments_serializer= AppointmentSerializer(doctor_appointments,many=True)
    return Response(doctor_appointments_serializer.data)
