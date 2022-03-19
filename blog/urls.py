from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [

    path('', views.ArticleListView.as_view(), name="article-list"),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name="article-detail"),
    path('<int:pk>/vote/', views.article_vote, name="article-vote"),
    path('<int:pk>/like/', views.like_or_unlike_article, name="article-like"),
    path('<int:pk>/comment/', views.comment, name="article-comment"),

]