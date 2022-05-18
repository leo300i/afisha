from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=155),

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    descriptions = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кино'
        verbose_name_plural = 'кино'


class Review(models.Model):
    text = models.TextField(verbose_name='текст')
