from django.urls import path, include


urlpatterns = [
    path("doctors/", include("doctors.urls")),
    path("patients/", include("patients.urls")),

]
