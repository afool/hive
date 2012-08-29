from django.forms import ModelForm
from models import EmailActivation

class EmailRegistrationForm(ModelForm):
    class Meta:
        model = EmailActivation
        fields = ("email",)
