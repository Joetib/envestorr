import datetime
from stocks.utils import StocksService

from decimal import Decimal
from django.core.management.base import BaseCommand

from django.utils import timezone
from stocks.models import Company, StockEntry

S = StocksService()


class Command(BaseCommand):
    help = "Run background tasks"

    def handle(self, *args, **kwargs):
        time = timezone.now()
        self.stdout.write(f"Fetching stocks from API background tasks: {time}")
        stocks = S.live()
        date = time.date()
        opening_time = datetime.time(hour=10)
        if time.time() < opening_time:
            raise Exception(f"Cannot fetch stocks at {time}. Stocks open at {opening_time}")
        for data in stocks:
            print(data)
            
            
            company: Company = Company.objects.get_or_create(label=data['name'])[0]
            if not company.name:
                company.fetch_and_update()
                continue

            stock_entry_qs = StockEntry.objects.filter(company=company, date=date)
            if stock_entry_qs.exists():
                stock_entry = stock_entry_qs.first()
            else:
                stock_entry = StockEntry(date=date, company=company)
            if not stock_entry.opening_price:
                stock_entry.opening_price = data['price']
            stock_entry.price_change = data['change']
            stock_entry.closing_price = data['price']
            stock_entry.closing_bid_price = data['price']
            stock_entry.closing_offer_price = data['price']
            
                
            stock_entry.total_shares_traded = data['volume']
            stock_entry.total_value_traded = data['volume'] * data['price']
            stock_entry.save()

        end_time = timezone.now()
        self.stdout.write(f"Completed running News background tasks : {end_time}")
