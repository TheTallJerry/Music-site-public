from django import forms
from .models import ContactRequest
from captcha.fields import ReCaptchaField

class ContactRequestForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactRequest
        fields = ("title", "name", "subject", "comments", "email")
        