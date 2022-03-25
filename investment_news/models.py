from django.urls import reverse
from django.db import models

# Create your models here.

class BusinessNews(models.Model):
    author = models.CharField(blank=True, max_length=100)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    content = models.TextField()
    source = models.CharField(max_length=100)
    url_to_image = models.URLField()
    url = models.URLField()
    published_at =models.DateTimeField()

    class Meta:
        ordering = ('-published_at',)
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('investment_news:business-news-detail', kwargs={'pk': self.pk})