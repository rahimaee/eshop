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
    return f"brand/{final_name}"


class Brand(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام برند')
    url = models.CharField(max_length=120, verbose_name='ادرس در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    images = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.title
