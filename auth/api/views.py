from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

from auth.api.serializers import UserSerializer


@api_view(["POST"])
def register_new_user(request):
    data = request.data
    username = data["username"]
    password = data["password"]

    user = User.objects.create_user(
        username=username,
        password=password,
    )
    if "email" in data:
        user.email = data["email"]

    if "first_name" in data:
        user.first_name = data["first_name"]

    if "last_name" in data:
        user.last_name = data["last_name"]

    user.save()

    user_serializer = UserSerializer(user)

    return Response(user_serializer.data)
