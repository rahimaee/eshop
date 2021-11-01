from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.http import Http404
from eshop_products.models import Tag


# Create your views here.


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.get_active()


def products_detail(request, *args, **kwargs):
    product_name = kwargs['name']
    product_id = kwargs['productId']
    product = Product.objects.get_by_id(product_id)
    if product is None or not product.is_active:
        raise Http404()
    tag = product.Tag.all()
    context = {
        'product': product,
        'tag': tag
    }

    return render(request, 'products/product-details.html', context)


class SearchProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 2

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active()
