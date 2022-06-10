from django.urls import path

from . import views

app_name = "stocks"

urlpatterns = [
    path('', views.StocksList.as_view(), name='stocks-list'),
    path('company/<slug:slug>/', views.StockCompanyDetail.as_view(), name="stocks-company-detail"),
   
]
