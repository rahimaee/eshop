from django.contrib import admin
from .models import Product, Gallery


# Register your models here.
class ImageInline(admin.TabularInline):
    model = Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'is_active']
    inlines = [
        ImageInline
    ]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(Gallery)
