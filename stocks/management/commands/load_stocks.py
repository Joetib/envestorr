from decimal import Decimal
from django.core.management.base import BaseCommand

from django.utils import timezone
from stocks.models import Company, StockEntry
from investment_news.utils import run
import csv

class Command(BaseCommand):
    help = "Run background tasks"

    def handle(self, *args, **kwargs):
        time = timezone.now()
        self.stdout.write(f"Running News background tasks: {time}")
        with open('data.csv') as file:
            reader = csv.reader(file.readlines())
            
            next(reader)
            for data in reader:
                if not data:
                    continue
                print(data)
                
                StockEntry(
                    date = data[0],
                    company=Company.objects.get_or_create(label=data[1])[0],
                    
                    
                    opening_price = Decimal(data[5].replace(',', '')),
                    closing_price = Decimal(data[6].replace(',', '')), 
                    price_change = Decimal(data[7].replace(',', '')),
                     closing_bid_price = Decimal(data[8].replace(',', '')) if data[8] else Decimal(0), 
                     closing_offer_price = Decimal(data[9].replace(',', '')) if data[9] else Decimal(0), 
                     total_shares_traded = data[10].replace(',', '') if data[10] else Decimal(0), 
                     total_value_traded = Decimal(data[11].replace(',', '')) if data[11] else Decimal(0),
                    
                ).save()
                
        end_time = timezone.now()
        self.stdout.write(f"Completed running News background tasks : {end_time}")