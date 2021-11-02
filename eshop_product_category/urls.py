from django.urls import path
from .views import category

app_name = "eshop_category"

urlpatterns = [
    path('product/category/<slug>', category, name='search'),
]
