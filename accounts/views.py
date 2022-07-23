from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.


class Dashboard(TemplateView):
    template_name: str = "accounts/dashboard.html"



class PortfolioList(ListView):
    pass