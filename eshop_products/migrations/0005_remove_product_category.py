# Generated by Django 3.2.8 on 2021-11-01 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]