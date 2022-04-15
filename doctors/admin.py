from tokenize import Special
from django.contrib import admin

from doctors.models import Doctor, Schedule, Specialization

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Schedule)
