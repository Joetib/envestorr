import datetime
from typing import Dict, List, Tuple
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import requests
from django.utils import timezone

from stocks.utils import StocksService
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    label = models.CharField(max_length=100)
    capital = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    industry = models.CharField(max_length=50, blank=True)
    sector = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=100, blank=True, help_text="phone numbers seperated by comma and space")
    shares = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    slug = models.SlugField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.label

    def last_thirty_days_stocks(self):
        date = timezone.now() - datetime.timedelta(days=30)
        stocks =  self.stock_entries.filter(date__gt=date.date())
        return stocks
    def get_telephone_numbers(self) -> List[str]:
        return [i.strip() for i in self.telephone.split(",")]
    def update_with_json(self, data: Dict) -> "Company":
        """Update the current company model with data fetched from the api.

        Sample data looks like
        --------

        -   {
                'capital': 11061426924.0,
                'company': {'address': 'MTN House, Independence Avenue, West Ridge, Accra, '  
                                        'Ghana',
                            'directors': [],
                            'email': 'customercare@mtn.com.gh',
                            'facsimile': None,
                            'industry': 'Mobile Telecommunications',
                            'name': 'Scancom Plc',
                            'sector': 'Telecommunications',
                            'telephone': '+233-24-430-0000, +233-24-100-62279',
                            'website': 'mtn.com.gh'},
                'dps': None,
                'eps': None,
                'name': 'MTNGH',
                'price': 0.9,
                'shares': 12290474360
            }
        
        """
        company_data: Dict = {key: value for key, value in data['company'].items() if value is not None}
        self.capital = data['capital']
        self.shares = data['shares']
        self.name = company_data['name']
        self.address = company_data.get("address", "")
        self.industry = company_data.get("industry", "")
        self.sector = company_data.get("sector", "")
        self.telephone = company_data.get("telephone", "")
        self.website = company_data.get("website", "")
        self.email = company_data.get("email", "")
        self.industry = company_data.get("industry", "")
        self.industry = company_data.get("industry", "")
        self.save()
        return self

    def fetch_and_update(self) -> Tuple[bool, str]:
        try:
            self.update_with_json(StocksService().equities_for_symbol(self.label))
            return True, "Successful"
        except requests.HTTPError:
            return False, "Update failed due to network issues."

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
            self.update_with_json()
        return super(Company, self).save(*args, **kwargs)
    
    def get_absolute_url(self) -> str:
        return reverse("stocks:stocks-company-detail", kwargs={"slug": self.slug})

    

class StockEntry(models.Model):
    company = models.ForeignKey(Company, related_name="stock_entries", on_delete=models.CASCADE)
    opening_price = models.DecimalField(max_digits=10, decimal_places=2)
    closing_price = models.DecimalField(max_digits=10, decimal_places=2)
    closing_bid_price = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    price_change = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    closing_offer_price = models.DecimalField(blank=True, max_digits=10, decimal_places=2)
    total_shares_traded = models.PositiveIntegerField(default=0)
    total_value_traded = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    
    date = models.DateField(default=datetime.datetime.today)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date", "company")

    def year_high(self):
        return self.opening_price # TODO: fix me
    
    def year_low(self):
        return 0 #TODO: fix this.

    def __str__(self) -> str:
        return f"Stock for {self.company.name} on {self.date}"
    