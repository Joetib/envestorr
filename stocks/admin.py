from django.contrib import admin

from stocks.models import Company, StockEntry

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("label", "name", "capital", "shares")

@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ("date", "company", "opening_price", "closing_price", "price_change", "closing_offer_price", "total_shares_traded", "total_value_traded", "year_high", "year_low")

    list_filter = ("date", "company")