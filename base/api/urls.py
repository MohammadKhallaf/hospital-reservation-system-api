from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from base.api.views import CustomTokenObtainPairView


urlpatterns = [
    path("auth/", include("authApp.api.urls"), name="auth_app"),
    path("doctors/", include("doctors.api.urls"), name="doctors_app"),
    path("patients/", include("patients.api.urls"), name="patients_app"),
    path("token/", CustomTokenObtainPairView.as_view(), name="generate_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
