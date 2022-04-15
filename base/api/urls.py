from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from base.api.views import MyTokenObtainPairView


urlpatterns = [
    path("auth/", include("authApp.api.urls")),
    path("doctors/", include("doctors.urls")),
    path("patients/", include("patients.urls")),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
