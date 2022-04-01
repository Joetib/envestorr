from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from investment_news.models import BusinessNews

# Create your views here.

class BusinessNewsList(ListView):
    model = BusinessNews
    queryset = BusinessNews.objects.all()
    paginate_by = 12
    context_object_name = "business_news_list"
    template_name = "business_news/business_news_list.html"

    def get_queryset(self):
        queryset = self.queryset
        self.search_term = self.request.GET.get("search", "")
        if self.search_term:
            queryset = queryset.filter(Q(title__icontains=self.search_term)|Q(description__icontains=self.search_term) | Q(content__icontains=self.search_term))
        return queryset
    
    def get_context_data(self):
        context = super().get_context_data()
        context['search_term'] = self.search_term
        return context

    

class BusinessNewsDetail(DetailView):
    model = BusinessNews
    queryset = BusinessNews.objects.all()
    context_object_name = "business_news"
    template_name = "business_news/business_news_detail.html"

