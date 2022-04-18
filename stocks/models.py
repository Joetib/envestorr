from datetime import datetime
from django.db import models
from pytz import timezone

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    label = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

    

class StockEntry(models.Model):
    comany = models.ForeignKey(Company, related_name="stock_entries", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ("date",)

    def __str__(self) -> str:
        return f"Stock for {self.company.name} on {self.date}"
    