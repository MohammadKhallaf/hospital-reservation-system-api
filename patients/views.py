from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from patients.models import Appointment
from patients.serializers import AppointmentSerializer

# Create your views here.

"""
Appointments EndPoint
"""


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_appointments(request):
    appointments = Appointment.objects.all()
    appointments_serializer = AppointmentSerializer(appointments, many=True)
    return Response(appointments_serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_appointment(request):
    data = request.data
    data["patient"] = request.user.id
    appointment_serializer = AppointmentSerializer(data=data)
    if appointment_serializer.is_valid():
        appointment_serializer.save()
        return Response(appointment_serializer.data)
    return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def edit_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
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
@permission_classes([IsAuthenticated])
def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return Response("Appointment Deleted")
