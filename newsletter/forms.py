from django import forms
from .models import NewsLeterContact
class NewsLetterContactForm(forms.ModelForm):
    class Meta:
        model = NewsLeterContact

        fields = ("first_name", "last_name", "email")