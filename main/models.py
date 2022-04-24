from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    file_book = models.FileField(upload_to="files/%Y/%m/%d")
    is_premium = models.BooleanField(default=False)

