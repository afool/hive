from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text = ("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",)
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2