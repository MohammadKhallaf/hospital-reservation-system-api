from django.db import models

DAYS_OF_WEEK = (
    ("sat", "Saturday"),
    ("sun", "Sunday"),
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday"),
)
GENDER = (
    ("male", "male"),
    ("female", "female"),
)


class Schedule(models.Model):

    doctor = models.ForeignKey(
        "Doctor", on_delete=models.CASCADE, related_name="doctor_schedules"
    )
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK, blank=True)
    time_from = models.TimeField()
    time_to = models.TimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.doctor} - Day: {self.day.capitalize()} | From {self.time_from} | To {self.time_from}"


class Specialization(models.Model):

    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Doctor(models.Model):

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=7, choices=GENDER,default='male')
    experience = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=30, unique=True)
    picture = models.ImageField(upload_to="images", null=True, blank=True)
    fees = models.DecimalField(max_digits=7, decimal_places=1,default=0)
    specialization = models.ForeignKey(
        "Specialization", related_name="doctors", on_delete=models.CASCADE
    )
    arrival_time = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
