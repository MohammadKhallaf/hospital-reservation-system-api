from functools import partial
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from doctors.models import Doctor, Specialization
from patients.models import Appointment

from doctors.api.serializers import (
    DoctorAppointmentSerializer,
    DoctorSerializer,
    SpecializationSerializer,
)
from patients.api.serializers import AppointmentSerializer


"""
Doctors Endpoint
"""


@api_view(["GET"])
def get_all_doctors(request):

    doctor = Doctor.objects.all()
    doctor_serializer = DoctorSerializer(doctor, many=True)

    return Response(doctor_serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_new_doctor(request):

    doctor_instance = Doctor.objects.create(**request.data)

    doctor_serializer = DoctorSerializer(doctor_instance)

    return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_doctor(request, pk):

    doctor = Doctor.objects.get(id=pk)
    doctor_serializer = DoctorSerializer(
        instance=doctor, data=request.data, partial=True
    )

    if doctor_serializer.is_valid():
        doctor_serializer.save()
        return Response(doctor_serializer.data, status=status.HTTP_200_OK)

    return Response(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_doctor(request, pk):

    doctor = Doctor.objects.get(id=pk)
    doctor.delete()

    return Response("deleted successfully")


"""
Doctors' Appointments
"""


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_doctor_appointments(request, pk):

    doctor = Doctor.objects.get(id=pk)

    doctor_appointments = Appointment.objects.filter(doctor=doctor)
    doctor_appointments_serializer = AppointmentSerializer(
        doctor_appointments, many=True
    )

    return Response(doctor_appointments_serializer.data)


"""
Specializations
"""


@api_view(["GET"])
def get_all_specializations(request):

    specs = Specialization.objects.all()
    spec_serializer = SpecializationSerializer(specs, many=True)

    return Response(spec_serializer.data)


@api_view(["GET"])
def get_specialization_doctors(request, pk):

    doctors = Doctor.objects.filter(specialization_id=pk)
    doctors_serializer = DoctorSerializer(doctors, many=True)

    return Response(doctors_serializer.data)


"""
Doctor report
"""


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_date_appointments(request, pk):

    appointments = Appointment.objects.filter(doctor_id=pk, date=request.data["date"])
    appointment_serializer = DoctorAppointmentSerializer(appointments, many=True)

    return Response(appointment_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_appointments(request):

    appointments = Appointment.objects.all().order_by("-date")
    appointment_serializer = DoctorAppointmentSerializer(appointments, many=True)

    return Response(appointment_serializer.data)
