from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("problem/", views.problem, name="problem"),
    path("solutions/", views.solutions, name="solutions"),
    path("sources/", views.sources, name="sources"),
]
