from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="home"),
    path('catalog/', views.catalog, name="catalog")
]
