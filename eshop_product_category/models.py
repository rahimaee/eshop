import os
from random import randint

from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from eshop_product_category.utils import unique_slug_generator
from eshop_tag.models import Tag


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"product/category/{final_name}"


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(verbose_name='توضیحان')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Tag = models.ManyToManyField(Tag, blank=True)
    url = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return f"{reverse('category_url:search')}{self.slug}/{self.title.replace(' ', '-')}"


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)
