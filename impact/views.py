# impact/views.py

from django.shortcuts import render

def home(request):
    return render(request, "impact/home.html")

def problem(request):
    return render(request, "impact/problem.html")

def solutions(request):
    return render(request, "impact/solutions.html")

def sources(request):
    return render(request, "impact/sources.html")
