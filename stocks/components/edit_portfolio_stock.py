from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from stocks.models import Company, PortFolio, PortFolioStock, User


class EditPortfolioStockView(UnicornView):
    portfoliostock: PortFolioStock = None
    purchase_quantity: int = 0
    purchase_quantity_error_message: str = ""
    purchase_price: float = 0
    purchase_price_error_message: str = ""

    show: bool = False
    def __init__(self, portfoliostock: PortFolioStock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfoliostock = portfoliostock
        self.purchase_price = self.portfoliostock.purchase_price
        self.purchase_quantity = self.portfoliostock.quantity_purchased

    def toggle_show(self, **kwargs):
        self.show = not self.show

    

    def validate_values(self):
        self.purchase_price_error_message = ""
        self.purchase_quantity_error_message = ""

        is_valid = True
        if not self.purchase_price:
            is_valid = False
            self.purchase_price_error_message = "Please enter the price of a unique stock"
        if not self.purchase_quantity:
            is_valid = False
            self.purchase_quantity_error_message = "Please enter the quantity of stock you purchased."
        return is_valid


    def add_stock(self, *args, **kwargs):
        if not self.validate_values():
            return
        portfoliostock = self.portfoliostock
        portfoliostock.purchase_price = self.purchase_price
        portfoliostock.quantity_purchased = self.purchase_quantity
        portfoliostock.save()
        return redirect(self.portfoliostock.portfolio.get_absolute_url())
