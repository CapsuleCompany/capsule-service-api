from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.db import models
from core.helper import state_choices, country_choices


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Business(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(
        default="https://via.placeholder.com/150", blank=True, null=True
    )
    phone = models.CharField(max_length=15, blank=True)
    location = models.ManyToManyField("Address", related_name="locations", blank=True)
    service_radius = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(BaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()


class Address(BaseModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=state_choices)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(
        max_length=100, default="United States", choices=country_choices
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, editable=False
    )


class Subscription(BaseModel):
    occurrence = models.CharField(max_length=100)


class ServiceTime(BaseModel):
    min = models.IntegerField(null=True, blank=True)
    max = models.IntegerField(null=True, blank=True)
    estimate = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=100, blank=True)


class ServicePrice(BaseModel):
    amount = models.FloatField()
    name = models.CharField(max_length=100)
    service = models.ForeignKey(
        "Service",
        related_name="service_price",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    service_detail = models.ForeignKey(
        "ServiceDetail",
        related_name="additional_cost",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    is_subscribable = models.BooleanField(default=False)


class Service(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    subcategories = models.ManyToManyField(
        Subcategory, related_name="services", blank=True
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, null=True, blank=True
    )
    time_estimate = models.ForeignKey(
        ServiceTime, on_delete=models.CASCADE, null=True, blank=True
    )
    company = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name="offered_services"
    )
    image = models.URLField(
        default="https://via.placeholder.com/150", blank=True, null=True
    )
    customizable = models.BooleanField(default=False)
    default_options = models.ManyToManyField(
        "ServiceDetail", related_name="default_services", blank=True
    )

    def __str__(self):
        return self.name


class ServiceDetail(BaseModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="options"
    )
    time = models.ForeignKey(
        ServiceTime,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="additional_time",
    )
    image = models.URLField(
        default="https://via.placeholder.com/150", blank=True, null=True
    )

    def __str__(self):
        return self.name


class Detail(BaseModel):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    meta = models.TextField(blank=True)
    service_detail = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
