from django.shortcuts import redirect
from django_unicorn.components import UnicornView
from stocks.models import Company, PortFolio, PortFolioStock, User


class AddPortfolioStockView(UnicornView):
    portfolio: PortFolio = None
    company: Company = None
    company_error_message : str = ""
    company_id: int = None
    companies = Company.objects.all()
    purchase_quantity: int = 0
    purchase_quantity_error_message: str = ""
    purchase_price: float = 0
    purchase_price_error_message: str = ""

    show: bool = False

    def __init__(self, portfolio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolio = portfolio

    def toggle_show(self, **kwargs):
        self.show = not self.show

    def updated_company_id(self, *args, **kwargs):
        if self.company_id:
            self.company = Company.objects.get(id=self.company_id)

        else:
            self.company = None

    def validate_values(self):
        self.company_error_message = ""
        self.purchase_price_error_message = ""
        self.purchase_quantity_error_message = ""

        is_valid = True
        if not self.company:
            is_valid = False
            self.company_error_message = "Please select a company"
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
        stock = PortFolioStock.objects.create(
            portfolio=self.portfolio,
            stock=self.company,
            quantity_purchased=self.purchase_quantity,
            purchase_price=self.purchase_price,
        )
        return redirect(self.portfolio.get_absolute_url())
