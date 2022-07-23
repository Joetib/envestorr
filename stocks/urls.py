from django.urls import path

from . import views

app_name = "stocks"

urlpatterns = [
    path('', views.StocksList.as_view(), name='stocks-list'),
    path('portfolio/', views.PortFolioList.as_view(), name="portfolio-list"),
    path('portfolio/<int:pk>/', views.PortFolioDetails.as_view(), name="portfolio-details"),
    path('company/<slug:slug>/', views.StockCompanyDetail.as_view(), name="stocks-company-detail"),
   
]
