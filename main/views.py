from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *


def main_page(request):
    return render(request, 'main/main_page.html')


def search_book(request):
    author_or_title = request.GET.get('search')
    book = Book.objects.filter(Q(title__icontains=author_or_title) | Q(author__icontains=author_or_title))
    paginator = Paginator(book, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(book) == 0:
        book = False

    context = {
        'book': book,
        'page_obj': page_obj
    }
    return render(request, 'main/search_book.html', context)


def pageNotFound(request, exception):
    return render(request, 'main/404.html')


def catalog(request):
    book = Book.objects.all()
    cat = Category.objects.all()
    paginator = Paginator(book, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(book) == 0:
        count_book = True
    else:
        count_book = False

    context = {
        'book': book,
        'cat': cat,
        'page_obj': page_obj,
        'cat_selected': 0,
        'count_book': count_book
    }
    return render(request, 'main/catalog.html', context=context)


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.is_premium:
        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)
            if book.is_premium == profile.premium:
                premium = True
            else:
                premium = False
        else:
            premium = False
    else:
        premium = True

    context = {
        'book': book,
        'premium': premium
    }
    return render(request, 'main/book.html', context=context)


def show_user(request):
    profile = Profile.objects.get(user_id=request.user.id)
    flag = profile.premium
    if request.method == "POST":
        if "premium" in request.POST:
            if profile.premium:
                profile.premium = False
                flag = False
            else:
                profile.premium = True
                flag = True

        profile.save()

    if request.user.is_staff == 1:
        staff = True
    else:
        staff = False

    context = {
        'profile': profile,
        'staff': staff,
        'flag': flag,
    }
    return render(request, 'main/User-cabinet.html', context)


def show_cat(request, cat_id):
    book = Book.objects.filter(cat_id=cat_id)
    cat = Category.objects.all()
    paginator = Paginator(book, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if len(book) == 0:
        count_book = True
    else:
        count_book = False

    context = {
        'book': book,
        'cat': cat,
        'page_obj': page_obj,
        'cat_selected': cat_id,
        'count_book': count_book
    }
    return render(request, 'main/catalog.html', context=context)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('user')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')