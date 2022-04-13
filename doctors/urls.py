from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_all_doctors, name="doctor list"),
    path("create/", views.create_new_doctor),
    path("update/<str:pk>", views.update_doctor),
    path("delete/<str:pk>", views.delete_doctor),
    path("appointments/<str:pk>", views.get_doctor_appointments),
]
