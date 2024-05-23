from allauth.account.forms import LoginForm
from django import forms


class CustomLoginForm(LoginForm):
    login = forms.EmailField(label='Email')

    def clean(self):
        email = self.cleaned_data.get('login')
        self.cleaned_data['email'] = email
        return super().clean()
