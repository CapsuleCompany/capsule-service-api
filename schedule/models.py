from django.db import models
from django.conf import settings
from service.models import Service
from user.models import CustomUser as User
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Schedule(BaseModel):
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule #{self.id}"


class Appointment(BaseModel):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="appointments"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="appointments"
    )
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, related_name="appointments"
    )
    appointment_time = models.DateTimeField()
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
            ("completed", "Completed"),
        ],
        default="pending",
    )

    def __str__(self):
        return (
            f"Appointment #{self.id} for {self.service.name} on {self.appointment_time}"
        )


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Occurrence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(
        Event, related_name="occurrences", on_delete=models.CASCADE
    )
    occurrence_time = models.DateTimeField()

    def __str__(self):
        return f"{self.event.title} at {self.occurrence_time}"
