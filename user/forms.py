from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUser

class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=15, label='Phone Number', required=True)

    class Meta:
        model = CustomUser
        fields = ('phone', 'first_name', 'last_name', 'email')

    def save(self, request):
        user = super().save(request)
        user.phone = self.cleaned_data['phone']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    phone = forms.CharField(max_length=15, label='Phone Number', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].label = 'Phone Number'
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'placeholder': 'Phone Number'})

    def clean(self):
        phone = self.cleaned_data['login']
        password = self.cleaned_data['password']
        if phone and password:
            self.user = authenticate(phone=phone, password=password)
            if not self.user:
                raise forms.ValidationError("Invalid login")
        return self.cleaned_data
