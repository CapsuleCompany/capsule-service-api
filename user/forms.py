from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUser


class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=15, label='Phone Number')

    class Meta:
        model = CustomUser
        fields = ('phone',)

    def save(self, request):
        user = super().save(request)
        user.phone = self.cleaned_data['phone']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    phone = forms.CharField(max_length=15, label='Phone Number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'Phone Number'
