from django.contrib import admin

from patients.models import Appointment, Patient


# Register your models here.
admin.site.register(Patient)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time","created")
    list_filter = ("patient", "date")
    ordering = ("-created",)
