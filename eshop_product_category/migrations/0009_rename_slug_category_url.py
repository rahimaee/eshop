# Generated by Django 3.2.8 on 2021-11-02 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_category', '0008_remove_category_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='url',
        ),
    ]
