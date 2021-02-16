from django.shortcuts import render
from django.contrib import auth
from comment.forms import Search_Comment


def home(request):

    context = {'Search_Comment': Search_Comment()}
    return render(request, 'home.html', context)


def diagnosis(request):
    return render(request, 'diagnosis.html', {})


def search(request):
    return render(request, 'search.html', {})




