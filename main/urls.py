from django.urls import path
from . import views
from .views import LoginUser, RegisterUser

urlpatterns = [
    path('', views.main_page, name="home"),
    path('catalog/', views.catalog, name="catalog"),
    path('book/<int:book_id>/', views.show_book, name="book"),
    path('category/<int:cat_id>/', views.show_cat, name="category"),
    path('search/', views.search_book, name="search"),
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register")
]
