from django.urls import path

from . import views

app_name  = "financial_tools"

urlpatterns = [path("", views.CurrencyConverter.as_view(), name="currency-converter"),
]