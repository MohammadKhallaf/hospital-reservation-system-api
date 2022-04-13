from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_all_doctors, name="doctor list"),
    path("add/", views.create_new_doctor),
    path("update/<str:pk>", views.update_doctor),
    path("del/<str:pk>", views.delete_doctor),
]
