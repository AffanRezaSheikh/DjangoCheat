# mail/forms.py  (create this file)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# added: views.py imports MailForm, but the manual never defines it
class MailForm(forms.Form):
    recipient = forms.EmailField()
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
