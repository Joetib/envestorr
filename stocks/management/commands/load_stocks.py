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
        with open('data1.csv') as file:
            reader = csv.reader(file.readlines())
            
            next(reader)
            for data in reader:
                print(data)
                
                StockEntry(
                    date = data[0],
                    company=Company.objects.get_or_create(label=data[1])[0],
                    year_high=Decimal(data[2].replace(',', '')),
                    year_low = Decimal(data[3].replace(',', '')),
                    
                    opening_price = Decimal(data[5].replace(',', '')),
                    closing_price = Decimal(data[6].replace(',', '')), 
                    price_change = Decimal(data[7].replace(',', '')),
                     closing_bid_price = Decimal(data[8].replace(',', '')) if data[8] else Decimal(0), 
                     closing_offer_price = Decimal(data[9].replace(',', '')) if data[9] else Decimal(0), 
                     total_shares_traded = data[10].replace(',', ''), 
                     total_value_traded = Decimal(data[11].replace(',', '')),
                    
                ).save()
                
        end_time = timezone.now()
        self.stdout.write(f"Completed running News background tasks : {end_time}")