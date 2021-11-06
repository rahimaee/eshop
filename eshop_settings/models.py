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
    return f"SiteSettings/{final_name}"


class SiteSettings(models.Model):
    SiteName = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=400, verbose_name='ادرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about = models.TextField(verbose_name='درباره ما', default='درباره ما')
    logo = models.ImageField(upload_to=upload_image_path, blank=True, default='')
    CopyRight = models.CharField(max_length=150, verbose_name='کپی رایت سایت')
    map = models.ImageField(upload_to=upload_image_path, blank=True, default='')

    class Meta:
        verbose_name = 'تنضیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.SiteName
