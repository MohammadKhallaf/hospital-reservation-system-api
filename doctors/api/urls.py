from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_doctors, name="doctors_list"),
    path("create/", views.create_new_doctor),
    path("update/<str:pk>", views.update_doctor),
    path("delete/<str:pk>", views.delete_doctor),
    path("appointments/", views.get_all_appointments),
    path("appointments/<str:pk>", views.get_doctor_appointments),
    path("specializations/", views.get_all_specializations),
    path("specializations/<str:pk>", views.get_specialization_doctors),
    path("<str:pk>/pdf/", views.get_date_appointments),
]
