from django.contrib import admin

from financial_tools.models import Currency

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("symbol", "name", "rate")
    search_fields = ("Symbol", "name")
    list_filter= ("symbol", "name", "rate")
