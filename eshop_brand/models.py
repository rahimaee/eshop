from django.db import models


# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
