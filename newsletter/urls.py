from django.urls import path
from . import views
app_name = "newsletter"


urlpatterns = [
    path("", views.newsletter, name="newsletter"),
    path("subscribe/", views.subscribe, name="subscribe"),
]