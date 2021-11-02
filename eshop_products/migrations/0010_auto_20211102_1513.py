# Generated by Django 3.2.8 on 2021-11-02 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_category', '0009_rename_slug_category_url'),
        ('eshop_products', '0009_auto_20211102_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop_product_category.category'),
            preserve_default=False,
        ),
    ]
