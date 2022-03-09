from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('investment-opportunities/', views.InvestmentListView.as_view(), name="investment-opportunity-list"),
    path('investment-opportunity/<int:pk>/', views.InvestmentDetailView.as_view(), name="investment-opportunity-detail"),
]
