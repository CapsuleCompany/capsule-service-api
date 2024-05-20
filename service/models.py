import uuid
from django.db import models
# from django.contrib.auth.models import User


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
    location = models.OneToOneField('Location', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.URLField(default='https://via.placeholder.com/150', blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceDetail(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    provider = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Detail(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    meta = models.TextField()
    price = models.FloatField()
    service = models.ForeignKey(ServiceDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Detail, on_delete=models.CASCADE)
    meta = models.TextField()

    def __str__(self):
        return f"Order #{self.id}"


class Schedule(BaseModel):
    vendor_id = models.UUIDField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule #{self.id}"


# class CompanyReview(BaseModel):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
#     comment = models.TextField()
#
#     def __str__(self):
#         return f"Review for {self.company.name} by {self.reviewer.username}"
#
#
# class UserReview(BaseModel):
#     reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed_user')
#     reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
#     rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
#     comment = models.TextField()
#
#     def __str__(self):
#         return f"Review for {self.reviewed_user.username} by {self.reviewer.username}"
