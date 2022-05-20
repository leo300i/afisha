from django.db import models


# Create your models here.

class Director(models.Model):
    class Meta:
        verbose_name = 'директор'
        verbose_name_plural = 'директор'
    name = models.CharField(max_length=155),


    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    descriptions = models.TextField(verbose_name='Описание')
    Director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кино'
        verbose_name_plural = 'кино'


class Review(models.Model):
    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'

    text = models.TextField(verbose_name='текст')
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
