from django.shortcuts import render, redirect


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


# home page
def home_page(request):
    context = {
        'data': 'data'
    }
    return render(request=request, template_name="home_page.html", context=context)
