# Generated by Django 3.2.8 on 2021-11-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]