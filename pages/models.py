from operator import truediv
from django.db import models
from ckeditor.fields import RichTextField
from bs4 import BeautifulSoup
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="team_members/%Y/")
    position = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)

class InvestmentOpportunity(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    url = models.URLField()
    picture = models.ImageField(upload_to='investment/%Y/', null=True, blank=True)
    tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-last_modified",)
        verbose_name_plural = "Investment Opportunities"

    def __str__(self) -> str:
        return self.title

    def get_description_text(self) -> str:
        return BeautifulSoup(self.description).text

    def get_absolute_url(self) -> str:
        return reverse('investment-opportunity-detail', kwargs={'pk': self.pk})
    