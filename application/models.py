import datetime
import os

from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
from urllib.request import urlretrieve, urlopen

from django.utils.text import slugify


class Images(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField(blank=True, null=True,upload_to='images', verbose_name='Загрузить изображение')
    url = models.URLField(blank=True, null=True, verbose_name='Ссылка на изображение')

    def __str__(self):
        return str(self.id)

