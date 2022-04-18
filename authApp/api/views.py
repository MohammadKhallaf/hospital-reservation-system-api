from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from patients.models import Patient

from authApp.api.serializers import UserSerializer


@api_view(["POST"])
def register_new_user(request):
    data = request.data
    user = User.objects.create_user(**data)
    data["name"] = f"{data['first_name']} {data['last_name']}"

    user.save()
    patient_instance = Patient.objects.create(user=user, name=data["name"])
    user_serializer = UserSerializer(user)

    return Response(user_serializer.data)
