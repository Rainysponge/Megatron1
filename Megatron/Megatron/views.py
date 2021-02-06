from django.shortcuts import render
from django.contrib import auth


def home(request):
    return render(request, 'home.html', {})


def diagnosis(request):
    return render(request, 'diagnosis.html', {})


def search(request):
    return render(request, 'search.html', {})
