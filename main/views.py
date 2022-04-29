from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'main/main_page.html')


def pageNotFound(request, exception):
    return HttpResponse('Страница не найдена')


def catalog(request):
    book = Book.objects.all()
    cat = Category.objects.all()
    paginator = Paginator(book, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'book': book,
        'cat': cat,
        'page_obj': page_obj,
        'cat_selected': 0,
    }
    return render(request, 'main/catalog.html', context=context)


def show_book(request, book_id):
    return HttpResponse("Подробнее")


def show_cat(request, cat_id):
    book = Book.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()
    paginator = Paginator(book, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #if len(book) == 0:
        #raise Http404()

    context = {
        'book': book,
        'cat': cat,
        'page_obj': page_obj,
        'cat_selected': cat_id
    }
    return render(request, 'main/catalog.html', context=context)
