# impact/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.home, name="home"),

    # Other pages
    path("problem/", views.problem, name="problem"),
    path("solutions/", views.solutions, name="solutions"),
    path("sources/", views.sources, name="sources"),
]
