# Generated by Django 3.2.8 on 2021-11-08 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import eshop_news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop_tag', '0003_auto_20211103_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان خبر')),
                ('image', models.ImageField(upload_to=eshop_news.models.upload_image_path)),
                ('description', models.TextField(verbose_name='متن خبر')),
                ('time', models.DateTimeField(blank=True, verbose_name='تاریخ ثبت')),
                ('tag', models.ManyToManyField(to='eshop_tag.Tag', verbose_name='برچسب')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'اخبار',
                'verbose_name_plural': 'خبرها',
            },
        ),
    ]
