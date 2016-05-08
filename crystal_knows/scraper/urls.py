from django.conf.urls import url
from scraper import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.ScraperCrystalKnows.as_view(), name='scraped-info'),
]
