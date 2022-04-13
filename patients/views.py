from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from patients.models import Appointment
from patients.serializers import AppointmentSerializer

# Create your views here.

"""
Appointments EndPoint
"""


@api_view(["GET"])
def get_all_appointments(request):
    appointments = Appointment.objects.all()
    appointments_serializer = AppointmentSerializer(appointments, many=True)
    print(appointments)
    return Response(appointments_serializer.data)


@api_view(["POST"])
def create_appointment(request):
    appointment_serializer = AppointmentSerializer(data=request.data)
    if appointment_serializer.is_valid():
        appointment_serializer.save()
        return Response(appointment_serializer.data)
    return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def edit_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    print(request.data)
    appointment_serializer = AppointmentSerializer(
        instance=appointment,
        data={"date": request.data["date"], "time": request.data["time"]},
        partial=True,
    )
    if appointment_serializer.is_valid():
        appointment_serializer.save()
        return Response(appointment_serializer.data, status=status.HTTP_200_OK)
    return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return Response("Appointment Deleted")
