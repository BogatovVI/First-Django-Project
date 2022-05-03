from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Book(models.Model):
    author = models.CharField(max_length=255, null=True, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(verbose_name="Контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото книги")
    file_book = models.FileField(upload_to="files/%Y/%m/%d", verbose_name="Файл книги")
    is_premium = models.BooleanField(default=False, verbose_name="Премиум")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user/%Y/%m/%d/")
    premium = models.BooleanField(default=False, verbose_name="Подписка")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
