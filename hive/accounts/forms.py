from django.forms import ModelForm
from django.contrib.auth.models import User
from models import EmailActivation

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ("email", "password",)

class EmailRegistrationForm(ModelForm):
    class Meta:
        model = EmailActivation
        fields = ("email",)
