from random import randint
from django.db import models
import os
from django.shortcuts import reverse
from django.db.models import Q


# Create your models here.
# image name on  server
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"product/{final_name}"


class ProductManager(models.Manager):
    def get_active(self):
        return self.get_queryset().filter(is_active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().filter(lookup, is_active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحان')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('products_url:list')}{self.id}/{self.title.replace(' ', '-')}"
