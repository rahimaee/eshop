"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from eshop_order.views import send_request, verify
from .views import home_page, header, footer, sliders, about_page

urlpatterns = [
    path('', home_page, name='starting_page'),
    path('', include('eshop_product_category.urls', namespace='category_url')),
    path('products/', include('eshop_products.urls', namespace='products_url')),
    path('news/', include('eshop_news.urls', namespace='news-url')),
    path('', include('eshop_order.urls')),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('account/', include('eshop_account.urls', namespace='account')),
    path('contact-us/', include('eshop_contact.urls', namespace='contact')),
    path('sliders', sliders, name='sliders'),
    path('about-us', about_page, name='about-us'),
    path('request/', send_request, name='request'),
    path('verify/', verify, name='verify'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
