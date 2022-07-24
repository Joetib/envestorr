from django.shortcuts import redirect
from django_unicorn.components import UnicornView

from stocks.models import PortFolio


class EditPortfolioView(UnicornView):
    portfolio: PortFolio = None
    title: str = ""
    title_error_message: str = ""
    details: str = ""
    details_error_message: str = ""
    show: bool = False
    def __init__(self, portfolio: PortFolio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolio = portfolio
        self.title = portfolio.title
        self.details = portfolio.details

    def toggle_show(self, **kwargs):
        self.show = not self.show

    

    def validate_inputs(self):
        self.title_error_message = ""
        self.details_error_message = ""
        error = False
        print(self.title, self.details, "title-details")
        if len(self.title) < 2:
            self.title_error_message = "Please ensure the title is more than 2 characters long"
            error = True
        if not self.details:
            self.details_error_message = "Please enter a detailed description"
            error = True
        return error

    def save_portfolio(self, *args, **kwargs):
        if  self.validate_inputs():
            return
        if not self.request.user.is_authenticated:
            self.error_message = "Please log in to continue"
            return
        portFolio: PortFolio = self.portfolio
        portFolio.title = self.title
        portFolio.details = self.details
        portFolio.save()
        return redirect(portFolio.get_absolute_url())