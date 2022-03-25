from . import views
from django.urls import path

app_name = "investment_news"
urlpatterns = [
    path("", views.BusinessNewsList.as_view(), name="business-news-list"),
    path("<int:pk>/", views.BusinessNewsDetail.as_view(), name="business-news-detail"),
]
