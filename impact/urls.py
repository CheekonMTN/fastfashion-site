# impact/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.home, name="home"),
    # Sitemap
    path("sitemap.xml", views.sitemap, name="sitemap"),
    # Security.txt
    path(".well-known/security.txt", views.security_txt, name="security_txt"),
]
