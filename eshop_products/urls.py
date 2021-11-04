from django.urls import path
from .views import ProductsList, products_detail, SearchProductView, ProductsListByCategory, product_brand, \
    ProductBrandList, product_suggestion

app_name = "eshop_products"

urlpatterns = [
    path('', ProductsList.as_view(), name='list'),
    path('brand', product_brand, name='brand'),
    path('suggestion<productId>', product_suggestion, name='suggestion'),
    path('brand/<brand_url>', ProductBrandList.as_view(), name='brand_list'),
    path('<productId>/<name>', products_detail, name='detail'),
    path('search', SearchProductView.as_view(), name='search'),
    path('<category_name>', ProductsListByCategory.as_view(), name='category'),

]
