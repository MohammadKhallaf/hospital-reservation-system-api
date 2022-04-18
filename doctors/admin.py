from django.contrib import admin
from django.urls import reverse

from django.utils.http import urlencode
from django.utils.html import format_html

from doctors.models import Doctor, Schedule, Specialization


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "arrival_time", "view_students_link")

    def view_students_link(self, obj):
        count = obj.appointment_set.count()
        url = (
            reverse("admin:patients_appointment_changelist")
            + "?"
            + urlencode({"doctor__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Appointments</a>', url, count)

    view_students_link.short_description = "Appointments"


admin.site.register(Specialization)

admin.site.register(Schedule)
