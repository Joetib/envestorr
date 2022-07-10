
from typing import Dict
from .models import Currency
import requests
from django.conf import settings
class ExchangeRateService:
    BASE_URL =  "https://api.apilayer.com/exchangerates_data/"
    headers= {
        "apikey": settings.CURRENCY_API_KEY
    }

    def convert(self, to: str, from_: str, amount: float) :
        url = self.BASE_URL + f"convert?to={to};from={from_};amount={amount}"
        data = requests.get(url, headers=self.headers).json()
        return data['success'], data['result']

    def symbols(self):
        url = self.BASE_URL + "symbols"
        data = requests.get(url, headers=self.headers).json()
        return data['success'], data['symbols']
    
    def rates(self, base="GHS"):
        url = self.BASE_URL + f"latest?base={base}"
        data = requests.get(url, headers=self.headers).json()
        return data['success'], data['rates']




def fetch_currency_information():
    data: Dict[str, str]
    success, data  =  ExchangeRateService().symbols()
    if not success:
        print("Service call failed")
        return
    for symbol, name in data.items():
        currency, _ = Currency.objects.get_or_create(symbol=symbol, name=name)
    print("Saved currency data")



def fetch_rates():
    data: Dict[str, float]
    currency = Currency
    print("Updating rates.")
    success, data = ExchangeRateService().rates()
    if not success:
        print("Service call failed.")
        return
    print("Saving rates to database")
    for symbol, rate in data.items():
        print("Symbols>>> ", symbol, rate)
        currency, created = Currency.objects.get_or_create(symbol=symbol)
        currency.rate = rate
        currency.save()
        if created:
            print("Calling fetch_currency_information because a new currency is found.")
            fetch_currency_information()
    print("Done updating rates.")
    

    