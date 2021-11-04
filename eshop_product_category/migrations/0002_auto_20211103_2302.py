# Generated by Django 3.2.8 on 2021-11-03 19:32

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_tag', '0001_initial'),
        ('eshop_product_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Tag',
            field=models.ManyToManyField(blank=True, to='eshop_tag.Tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='eshop_product_category.category', verbose_name='دسته بندی مادر'),
        ),
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=120, unique=True, verbose_name='آدرس در url'),
        ),
    ]