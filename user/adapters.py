from allauth.account.adapter import DefaultAccountAdapter
from user.forms import CustomLoginForm


class CustomAccountAdapter(DefaultAccountAdapter):
    @staticmethod
    def get_login_form_class(self):
        return CustomLoginForm
