from django.contrib.auth.models import AbstractBaseUser
from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.conf import settings
from user.manager import CustomUserManager


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[RegexValidator(r"^\d{1,15}$", "Enter a valid phone number.")],
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
        ]
        ordering = ["email"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("contractor", "Contractor"),
        ("general", "General User"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(r"^\d{1,15}$", "Enter a valid phone number.")],
    )
    business = models.ManyToManyField("service.Business", blank=True)
    location = models.ManyToManyField("service.Address", blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="profile_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="profile_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        ordering = ["user__email"]

    def __str__(self):
        return self.user.email


class Notification(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.email} at {self.sent_at}"
