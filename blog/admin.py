from django.contrib import admin
from .models import ArticleCategory, Article, ArticleComment, ArticleVote
# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(ArticleComment)
admin.site.register(Article)
admin.site.register(ArticleVote)