from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Configuration(models.Model):
    about_us = RichTextField()
    disclaimer = RichTextField()
    terms_and_conditions = RichTextField()

    @classmethod
    def object() -> "Configuration":
        return Configuration.objects.get_or_create(id="1")[0]
