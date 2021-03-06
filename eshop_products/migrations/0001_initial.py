# Generated by Django 3.2.8 on 2021-11-03 00:19

from django.db import migrations, models
import eshop_products.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_product_category', '0001_initial'),
        ('eshop_tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='تصویر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('Tag', models.ManyToManyField(blank=True, to='eshop_tag.Tag')),
                ('category', mptt.fields.TreeManyToManyField(blank=True, to='eshop_product_category.Category')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
