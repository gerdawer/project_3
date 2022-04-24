from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Film(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    actors = models.CharField(max_length=150)
    genres = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    author = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name='author_comments'
    )
    text = models.TextField()
    created = models.DateTimeField('Дата', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)
    name = models.CharField(max_length=50, null=True)


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    """Рейтинг"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_rating'
    )
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="фильм")


    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"