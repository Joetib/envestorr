
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields  import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
import bs4
from ckeditor.fields import RichTextField
from django.utils import timezone

User = get_user_model()
# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('blog:article-list') + f"?category={self.id}"

class Article(models.Model):
    author = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE)
    
    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='article-images/')
    content = RichTextField()
    categories = models.ManyToManyField(ArticleCategory, blank=True, symmetrical=True)
    is_draft = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified  = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-date_created', )
        
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'pk': self.pk})
    
    def get_comment_url(self):
        return reverse('blog:article-comment', kwargs={'pk': self.pk})
    
    def get_vote_url(self):
        return reverse('blog:article-vote', kwargs={'pk': self.pk})
    def evaluate_votes(self):
        return sum([vote.vote for vote in self.votes.all() ])

class ArticleComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.content

class ArticleVote(models.Model):
    VOTE_CHOICES = (
        (1,1),
        (-1,-1)
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_votes")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="votes")
    vote = models.IntegerField(choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('author', 'article')
