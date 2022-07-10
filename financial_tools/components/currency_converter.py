from decimal import Decimal
from django_unicorn.components import UnicornView
from financial_tools.models import Currency

class CurrencyConverterView(UnicornView):
    currencies = Currency.objects.all()
    amount: float = 0
    to :str = ""
    from_: str = ""
    result: float = 0

    def convert(self, *args, **kwargs):
        if self.to and self.from_:
            print(self.to, self.from_)
            self.result = round( Decimal(self.amount )* Currency.objects.get(symbol=self.to).rate / Currency.objects.get(symbol=self.from_).rate, 2)
    
    def updated(self, name, value):
        self.convert()
        return super().updated(name, value)



