from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('stocks/', include('stocks.urls', namespace="stocks")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('business-news/', include('investment_news.urls', namespace="investment_news")),
    path('newsletter/', include('newsletter.urls', namespace="newsletter")),
    path('financial-tools/', include('financial_tools.urls', namespace="financial_tools")),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
