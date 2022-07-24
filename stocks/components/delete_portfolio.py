from django.shortcuts import redirect
from django.urls import reverse
from django_unicorn.components import UnicornView

from stocks.models import PortFolio


class DeletePortfolioView(UnicornView):
    portfolio: PortFolio = None
    show: bool = False

    def __init__(self, portfolio: PortFolio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolio = portfolio

    def toggle_show(self, **kwargs):
        self.show = not self.show

    def delete_portfolio(self, **kwargs):
        self.portfolio.delete()
        return redirect(reverse("stocks:portfolio-list"))
