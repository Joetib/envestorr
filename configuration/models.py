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


class SiteSlide(models.Model):
    leading = models.CharField(max_length=100, help_text="Leading is the text that appears before the slide title")
    title = models.CharField(max_length=70, help_text="The bold part of the slide")
    trailing = models.CharField(max_length=200, help_text="Text below the title")
    picture = models.ImageField(upload_to="slides/%Y", help_text="The slide background picture")
    action_text = models.CharField(max_length=50, help_text="The text that shows inside the slide button")
    action_url = models.URLField(help_text="the link that the button should go to.")
    active = models.BooleanField(default=True, help_text="Tells whether the slide should show on the side.")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-date_created",)

    def __str__(self) -> str:
        return self.title
