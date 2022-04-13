from tokenize import Special
from django.contrib import admin

from doctors.models import Doctor, Specializaion

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specializaion)
