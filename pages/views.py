from django.http import HttpRequest, QueryDict
from django.db.models import Q
from django.shortcuts import get_object_or_404

from blog.models import Article
from configuration.models import SiteSlide
from investment_news.models import BusinessNews
from . import models
from taggit.models import Tag
from django.views.generic import TemplateView, ListView, DetailView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()[:6]
        context['slides'] = SiteSlide.objects.filter(active=True)
        context['business_news_list'] = BusinessNews.objects.all()
        context['investment_opportunities'] = models.InvestmentOpportunity.objects.all()[:6]
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = models.TeamMember.objects.all()
        return context

class TermsAndConditionsView(TemplateView):
    template_name = "pages/terms_and_conditions.html"


class InvestmentListView(ListView):
    model = models.InvestmentOpportunity
    queryset = models.InvestmentOpportunity.objects.all()
    context_object_name = "investment_opportunities"
    paginate_by = 12
    template_name = "pages/investment_opportunity_list.html"
    search_query = ""
    tag = None

    def get_queryset(self):
        request: HttpRequest = self.request
        queryset = self.queryset
        self.search_query = request.GET.get("search", "")
        tag = request.GET.get('tag')
        if tag:
            
            self.tag = get_object_or_404(Tag, name=tag.strip())
            queryset = queryset.filter(tags=self.tag)
        if self.search_query:
            queryset = queryset.filter(
                *[Q(title__icontains=word) for word in self.search_query.split()]
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.search_query
        context['selected_tag'] = self.tag
        context['tags'] = Tag.objects.all()
        return context


class InvestmentDetailView(DetailView):
    model = models.InvestmentOpportunity
    queryset = models.InvestmentOpportunity.objects.all()
    context_object_name = "investment_opportunity"
    template_name = "pages/investment_opportunity_detail.html"
