import uuid
from django.db import models

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
        ('general', 'General User'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username


class Company(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.address_1}, {self.city}, {self.state}, {self.country}"


class Service(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='offered_services')
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceDetail(BaseModel):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.IntegerField(null=True, blank=True)
    duration_min = models.IntegerField(null=True, blank=True)
    duration_max = models.IntegerField(null=True, blank=True)
    provider = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='options')
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)

    def __str__(self):
        return self.name


class Detail(BaseModel):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    meta = models.TextField(blank=True)
    price = models.FloatField(null=True, blank=True)
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE, related_name='user_inputs')

    def __str__(self):
        return self.title


class Review(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.service.name}"


class Order(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Detail, on_delete=models.CASCADE)
    meta = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"


class Schedule(BaseModel):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule #{self.id}"


class Address(BaseModel):
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_1}, {self.city}, {self.state}, {self.country}"
