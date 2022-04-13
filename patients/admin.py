from django.contrib import admin

from patients.models import Appointment, Patient

# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
