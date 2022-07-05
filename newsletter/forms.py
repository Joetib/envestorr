from django import forms
from .models import NewsLeterContact
class NewsLetterContactForm(forms.ModelForm):
    class Meta:
        model = NewsLeterContact

        fields = ( "email",)