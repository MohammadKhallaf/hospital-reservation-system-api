from django.contrib import admin

from patients.models import Appointment, Patient

# class AppointmentAdmin(admin.ModelAdmin):
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


# Register your models here.
# admin.site.register(Patient)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time", "created")
    list_filter = ("patient", "date")
    ordering = ("-created",)
