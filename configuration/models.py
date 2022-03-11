from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Configuration(models.Model):
    about_us = RichTextField()
    disclaimer = RichTextField()
    terms_and_conditions = RichTextField()

    def __str__(self) -> str:
        return "Site Configuration"

    @classmethod
    def object(cls) -> "Configuration":
        return Configuration.objects.get_or_create(id="1")[0]
    
    def save(self, *args, **kwargs):
        self.id = 1
        super().save()
