import uuid
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Abstract base model with key information and UUID as default primary key.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('contractor', 'Contractor'),
        ('customer', 'Customer'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(BaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"


class Service(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServiceDetail(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    meta = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"


class Schedule(BaseModel):
    vendor_id = models.UUIDField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule #{self.id}"
