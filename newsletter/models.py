from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class NewsLeterContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "NewsLetter Contacts"
        ordering = ("first_name", "date_created")
        
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



class NewsLetter(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="newsletter/images/", blank=True)
    content = RichTextField()
    is_draft = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    sent_to= models.ManyToManyField(NewsLeterContact, related_name="newsletters", blank=True)


    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetters"
    
    def __str__(self):
        return self.title

    
    

