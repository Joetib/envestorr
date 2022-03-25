from django.views.generic import ListView, DetailView
from django.shortcuts import render

from investment_news.models import BusinessNews

# Create your views here.

class BusinessNewsList(ListView):
    model = BusinessNews
    queryset = BusinessNews.objects.all()
    paginate_by = 12
    context_object_name = "business_news_list"
    template_name = "business_news/business_news_list.html"


class BusinessNewsDetail(DetailView):
    model = BusinessNews
    queryset = BusinessNews.objects.all()
    context_object_name = "business_news"
    template_name = "business_news/business_news_detail.html"

