# Generated by Django 3.2.8 on 2021-11-03 19:19

from django.db import migrations, models
import eshop_brand.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_brand.models.upload_image_path, verbose_name='تصویر'),
        ),
    ]
