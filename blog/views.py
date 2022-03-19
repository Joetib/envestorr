from django.db.models import Q
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.contrib import messages
from django.utils import timezone
from . import forms
import json
from .import models
# Create your views here.


class ArticleListView(ListView):
    queryset = models.Article.objects.filter(is_draft=False)
    template_name = "core/article_list.html"
    context_object_name = "articles"
    category = None
    paginate_by = 24

    def get_queryset(self):
        queryset = self.queryset
        category_id = self.request.GET.get("category")
        if category_id:
            self.category = get_object_or_404(models.ArticleCategory, pk=int(category_id))
            queryset = queryset.filter(categories=self.category)
        self.search_term = self.request.GET.get("search", "")
        if self.search_term:
            queryset = queryset.filter(Q(title__icontains=self.search_term)| Q(content__icontains=self.search_term))
        return queryset
        

    def get_context_data(self):
        context = super().get_context_data()
        context['article_categories'] = models.ArticleCategory.objects.all()
        context['selected_category'] = self.category
        context['search_term'] = self.search_term
        return context

class ArticleDetailView(DetailView):
    model = models.Article
    queryset = models.Article.objects.filter(is_draft=False)
    context_object_name='article'
    template_name = "core/article_detail.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.CommentForm()
        return context

@login_required
def article_vote(request: HttpRequest, pk) -> HttpResponse:
    if request.method == "POST":
        article = get_object_or_404(models.Article, pk=pk)
        articlevote = models.ArticleVote.objects.get_or_create(article=article, author = request.user)[0]
        print(articlevote)
        vote = json.loads(request.body)
        if vote < -1 or vote > 1:
            raise Http404("Vote must be between 0 and 1")
        articlevote.vote = int(vote)
        articlevote.save()
    return JsonResponse({
        'votes': article.evaluate_votes(),
        'current_user_vote':vote,
    })

@login_required
def like_or_unlike_article(request: HttpRequest, pk) -> HttpResponse:
    unlike = bool(request.GET.get('unlike'))
    article = get_object_or_404(models.Article, pk=pk)
    if unlike:
        article.remove_like(request.user)
    else:
        article.add_like(request.user)
    return JsonResponse({
        'success': True,
        'liked': not unlike,
        'likes_count': article.liked_by.count(),

    })
        
@login_required
def comment(request: HttpRequest, pk: int) -> HttpResponse:
    article = get_object_or_404(models.Article, pk=pk, is_draft=False)
    if not request.method == "POST":
        messages.error(request, "only post requests allowed.")
    else:
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment: models.ArticleComment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.success(request, "Comment saved successfully")
        else:
            messages.error(request, "Your comment could not be saved. Kindly fix the errors in the form.") 
            messages.error(request, comment_form.errors.as_text())
    return redirect(article.get_absolute_url())
