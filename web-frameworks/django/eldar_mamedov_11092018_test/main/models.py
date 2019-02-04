from django.db import models

# Create your models here.


class A(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    city = models.ManyToManyField('City')


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
