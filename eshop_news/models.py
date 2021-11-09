import os
from random import randint

from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
from django.urls import reverse

from eshop_tag.models import Tag


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"news/{final_name}"


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', default=User.pk)
    title = models.CharField(max_length=100, verbose_name='عنوان خبر')
    image = models.ImageField(upload_to=upload_image_path)
    description = models.TextField(verbose_name='متن خبر')
    time = models.DateTimeField(blank=True, verbose_name='تاریخ ثبت')
    tag = models.ManyToManyField(Tag, verbose_name='برچسب')

    class Meta:
        verbose_name = 'اخبار'
        verbose_name_plural = 'خبرها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('eshop_news:home_news')}{self.id}/{self.title.replace(' ', '-')}"

    def get_user_name(self):
        user = User.objects.filter(pk=self.user_id).first()
        return f"نویسنده: {user.first_name}"
