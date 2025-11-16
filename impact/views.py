from django.shortcuts import render
from .models import HeadlineStat

def home(request):
    return render(request, "impact/home.html")

def problem(request):
    stats = HeadlineStat.objects.all()
    return render(request, "impact/problem.html", {"stats": stats})

def solutions(request):
    return render(request, "impact/solutions.html")

def sources(request):
    return render(request, "impact/sources.html")
