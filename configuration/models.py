from django.db import models
from ckeditor.fields import RichTextField
from .utils import phone_regex
# Create your models here.


class Configuration(models.Model):
    phone_number = models.CharField(
        max_length=15,
        help_text="must be 10-15 characters long",
        unique=True,
        default="+2331111111111",
        validators=[phone_regex],
    )
    email = models.EmailField(default="envestorr@envestorr.com")
    location = models.CharField(max_length=350, default="Kumasi")
    
    twitter_link = models.URLField(blank=True)
    whatsapp_link=models.URLField(blank=True)
    facebook_link=models.URLField(blank=True)
    linkedin_link=models.URLField(blank=True)
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
