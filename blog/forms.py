from typing import Any, Mapping, Optional
from django import forms
from django.core.files.base import File
from .models import ArticleComment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, Row, Column



class CommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ("content",)