from django.urls import path, include
from . import views

urlpatterns = [
   path("appointments/",views.get_all_appointments),
   path("appointments/create/",views.create_appointment),
   path("appointments/update/<str:pk>",views.edit_appointment),
   path("appointments/delete/<str:pk>",views.delete_appointment),
  

]
