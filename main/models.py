from django.db import models
from django.urls import reverse


class Book(models.Model):
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    file_book = models.FileField(upload_to="files/%Y/%m/%d")
    is_premium = models.BooleanField(default=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
