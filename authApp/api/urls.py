from django.urls import path
from .views import register_new_user

urlpatterns = [path("new/", register_new_user, name="register_user")]
