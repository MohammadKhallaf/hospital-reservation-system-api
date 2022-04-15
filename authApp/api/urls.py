from django.urls import path, include
from .views import register_new_user

urlpatterns = [path("new/", register_new_user)]
