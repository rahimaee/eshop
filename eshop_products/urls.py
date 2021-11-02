from django.urls import path
from .views import ProductsList, products_detail, SearchProductView,ProductsListByCategory

app_name = "eshop_products"

urlpatterns = [
    path('', ProductsList.as_view(), name='list'),
    path('<productId>/<name>', products_detail, name='detail'),
    path('search', SearchProductView.as_view(), name='search'),
    path('<category_name>', ProductsListByCategory.as_view(), name='category'),
]
