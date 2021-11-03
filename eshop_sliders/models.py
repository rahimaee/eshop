import os
from random import randint

from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"sliders/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='ادرس')
    description = models.TextField(verbose_name='توضیحات')
    images = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلادیر'
        verbose_name_plural = 'اسلادیرها'
