from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title')


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.site_title = "Админ-панель Library"
admin.site.site_header = "Админ-панель Library"
