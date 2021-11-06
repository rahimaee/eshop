from django.db import models


# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=50, verbose_name='عنوان پیام')
    message = models.TextField(verbose_name='پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده؟/نشده')

    class Meta:
        verbose_name = 'تماس باما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.message
