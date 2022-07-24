from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from stocks.models import PortFolioStock


class DeletePortfolioStockView(UnicornView):
    portfoliostock: PortFolioStock = None
    show: bool = False

    def __init__(self, portfoliostock: PortFolioStock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfoliostock = portfoliostock

    def toggle_show(self, **kwargs):
        self.show = not self.show

    def delete_stock(self, **kwargs):
        url = self.portfoliostock.portfolio.get_absolute_url()
        self.portfoliostock.delete()
        return redirect(url)
