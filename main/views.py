from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'main/main_page.html')


def catalog(request):
    posts = Book.objects.all()
    return render(request, 'main/catalog.html', {'posts': posts})
