from django.shortcuts import render
from django.views.generic import TemplateView

from financial_tools.models import Currency

# Create your views here.


class CurrencyConverter(TemplateView):
    template_name = "financial_tools/currency_converter.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['currencies'] = Currency.objects.all()
        return context


class InterestCalculator(TemplateView):
    template_name: str = "financial_tools/interest_calculator.html"
    