# impact/views.py

from django.shortcuts import render
from .models import HeadlineStat

def home(request):
    stats = HeadlineStat.objects.all()
    return render(request, "impact/home.html", {"stats": stats})
