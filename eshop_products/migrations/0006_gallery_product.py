# Generated by Django 3.2.8 on 2021-11-05 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_remove_product_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='eshop_products.product'),
            preserve_default=False,
        ),
    ]