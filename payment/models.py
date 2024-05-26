from django.db import models
from schedule.models import Appointment
from django.core.validators import MaxValueValidator, MinValueValidator
from service.models import Service
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.ForeignKey(
        "service.Address", on_delete=models.CASCADE, related_name="customers"
    )


class OrderType(BaseModel):
    choices = [
        ("once", "One Time"),
        ("weekly", "Bi-Weekly"),
        ("semi_monthly", "Semi-Monthly"),
        ("monthly", "Monthly"),
    ]
    name = models.CharField(max_length=50, choices=choices)

    def __str__(self):
        return self.name


class Order(BaseModel):
    status_options = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("in_progress", "In Progress"),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    is_subscription = models.BooleanField(default=False)
    stripe_subscription_id = models.CharField(
        max_length=255, blank=True, editable=False
    )
    status = models.CharField(max_length=50, default="pending", choices=status_options)
    order_number = models.CharField(max_length=100, unique=True, blank=True)
    service = models.ForeignKey(
        "service.Service",
        on_delete=models.CASCADE,
        related_name="orders",
        blank=True,
        null=True,
    )
    service_details = models.ManyToManyField(
        "service.ServiceDetail",
        related_name="orders",
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_type = models.ForeignKey(
        OrderType,
        on_delete=models.CASCADE,
        related_name="orders",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(uuid.uuid4()).replace("-", "").upper()[:12]
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.description


class Payment(BaseModel):
    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("failed", "Failed"),
        ],
        default="pending",
    )

    def __str__(self):
        return f"Payment #{self.id} for {self.appointment}"


class Review(BaseModel):
    service = models.ForeignKey(
        "service.Service", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey("payment.Order", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.email} for {self.service.name}"
