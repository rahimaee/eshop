from random import randint
from django.db import models
import os
from django.shortcuts import reverse
from django.db.models import Q
from mptt.fields import TreeForeignKey, TreeManyToManyField
from eshop_product_category.models import Category
from eshop_tag.models import Tag
from eshop_brand.models import Brand


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


def upload_image_gallery_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"product/gallery/{final_name}"


# class imagess(models.Model):
#     image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
#     is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
#     product = models.ForeignKey(Pr,on_delete=models.CASCADE, related_name="images")


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
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(Tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()

    def get_product_by_category(self, category_id):
        return self.get_queryset().filter(category__id=category_id).all()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحان')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    Tag = models.ManyToManyField(Tag, blank=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeManyToManyField(Category, blank=True)
    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{reverse('products_url:list')}{self.id}/{self.title.replace(' ', '-')}"

    def get_image_url(self):
        print(self.image)
        return f"/media/{self.image}"


class Gallery(models.Model):
    image = models.ImageField(upload_to=upload_image_gallery_path, null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
