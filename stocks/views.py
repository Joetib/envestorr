import json
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from typing import Dict, Any, List
from django.utils import timezone
import datetime
import pprint
from . import utils

# Create your views here.
class StocksList(ListView):

    model = models.StockEntry
    queryset = models.StockEntry.objects.order_by("-date")
    template_name = "stocks/stock_list.html"
    context_object_name = "stocks"
    paginate_by = 37 # the total number 

    def get_queryset(self):
        self.company = None
        self.start_date = None
        self.end_date = None
        queryset = super().get_queryset()
        today = timezone.now()

        start_date_arg = self.request.GET.get("start_date")
        end_date_arg = self.request.GET.get("end_date")
        company_arg = self.request.GET.get("company")
        if company_arg:
            company =get_object_or_404(models.Company, label=company_arg)
            queryset = queryset.filter(company=company)
            self.company = company
        if start_date_arg:
            start_date = datetime.date.fromisoformat(start_date_arg)
            queryset = queryset.filter(date__gte=start_date)
        else:
            start_date = None

        if end_date_arg:
            end_date = datetime.date.fromisoformat(end_date_arg)
        else:
            end_date = today.date()
        queryset = queryset.filter(date__lte=end_date)
        self.end_date = end_date
        self.start_date = start_date
        return queryset
        
        

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['end_date'] = self.end_date
        context['start_date'] = self.start_date
        context['company'] = self.company
        context['companies'] = models.Company.objects.all()
        return context


class StockCompanyDetail(DetailView):
    model = models.Company
    queryset = models.Company.objects.all()
    template_name = "stocks/stock_company_detail.html"
    context_object_name = "company"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        company: models.Company = self.get_object()
        # company.fetch_and_update()
        context = super().get_context_data(**kwargs)
        today = timezone.now()

        start_date_arg = self.request.GET.get("start_date")
        least_day = timezone.now() - datetime.timedelta(days=30)
        if start_date_arg:
            start_date = datetime.date.fromisoformat(start_date_arg)
        else:
            start_date = least_day.date()

        end_date_arg = self.request.GET.get("end_date")
        if end_date_arg:
            end_date = datetime.date.fromisoformat(end_date_arg)
        else:
            end_date = today.date()

        stock_data: List[models.StockEntry] = list(
            company.stock_entries.order_by("date").filter(
                date__lte=end_date, date__gte=start_date
            )
        )

        context['stocks'] = company.stock_entries.order_by("-date").filter(
                date__lte=end_date, date__gte=start_date
            )
        context["stocks_data"] = json.dumps(
            [float(stock.opening_price) for stock in stock_data]
        )
        context["stocks_labels"] = json.dumps([str(stock.date) for stock in stock_data])
        context["end_date"] = str(end_date)
        context["start_date"] = str(start_date)
        return context


class PortFolioList(LoginRequiredMixin,ListView):
    queryset = models.PortFolio.objects.all()
    paginate_by = 24
    template_name: str = "stocks/portfolio_list.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).distinct()


class PortFolioDetails(LoginRequiredMixin,DetailView):
    queryset = models.PortFolio.objects.all()
    template_name: str = "stocks/portfolio_details.html"
    context_object_name = "portfolio"
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)