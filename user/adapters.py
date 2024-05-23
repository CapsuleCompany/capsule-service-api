from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from .models import CustomUser


class CustomAccountAdapter(DefaultAccountAdapter):
    @staticmethod
    def clean_phone(self, phone):
        if CustomUser.objects.filter(phone=phone).exists():
            raise ValidationError('A user is already registered with this phone number.')
        return phone

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.phone = form.cleaned_data.get('phone')
        user.save()
        return user
