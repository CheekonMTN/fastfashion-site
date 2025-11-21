# fastfashion_site/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Send everything at the site root to the impact app
    path("", include("impact.urls")),
]
