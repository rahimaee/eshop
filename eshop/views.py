import itertools

from django.shortcuts import render, redirect
from eshop_sliders.models import Slider
from eshop_products.models import Product


# Header Code Behind
def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context=context)


# Footer Code Behind
def footer(request, *args, **kwargs):
    about_us = """این سایت فروشگاهی"""
    context = {
        'about_us': about_us
    }
    return render(request=request, template_name='shared/Footer.html', context=context)


# list _ group
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# home page
def home_page(request):
    product = Product.objects.all()
    last_product = list(my_grouper(4, product))
    context = {
        'data': 'data',
        'last_product': last_product,
    }
    return render(request=request, template_name="home_page.html", context=context)


def sliders(request, *args, **kwargs):
    all_slider_is_active = Slider.objects.get_queryset().filter(is_active=True).all()
    context = {
        'sliders': all_slider_is_active
    }
    return render(request, 'sliders_partial.html', context)
