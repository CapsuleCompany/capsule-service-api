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


class Profile(BaseModel):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('contractor', 'Contractor'),
        ('general', 'General User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    business = models.ForeignKey('Business', on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.user.username


class Business(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owned_businesses')

    def __str__(self):
        return self.name


class Roles(BaseModel):
    title = models.TextField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)


class BusinessRoles(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(BaseModel):
    address = models.OneToOneField("Address", on_delete=models.CASCADE, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Service(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategory, related_name='services')
    locations = models.ManyToManyField(Location, related_name='services')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='offered_services')
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceDetail(BaseModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.FloatField(null=True, blank=True)
    duration_min = models.IntegerField(null=True, blank=True)
    duration_max = models.IntegerField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='options')
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)

    def __str__(self):
        return self.name


class Detail(BaseModel):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    meta = models.TextField(blank=True)
    price = models.FloatField(null=True, blank=True)
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, related_name='meta')

    def __str__(self):
        return self.title


class Review(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.user.username} for {self.service.name}"


class Order(BaseModel):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service = models.ForeignKey(Detail, on_delete=models.CASCADE)
    meta = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"


class Schedule(BaseModel):
    vendor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule #{self.id}"


class Address(BaseModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_1}, {self.city}, {self.state}, {self.country}"


class ServiceHours(BaseModel):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_hours')
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.service.name} hours on {self.day}"


class Appointment(BaseModel):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='appointments')
    appointment_time = models.DateTimeField()
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ], default='pending')

    def __str__(self):
        return f"Appointment #{self.id} for {self.service.name} on {self.appointment_time}"


class Payment(BaseModel):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')

    def __str__(self):
        return f"Payment #{self.id} for {self.appointment}"


class Notification(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.user.username} at {self.sent_at}"


class ServiceAttribute(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service.name} - {self.name}: {self.value}"
