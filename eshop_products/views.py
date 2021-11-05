import itertools

from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Gallery
from django.http import Http404
from eshop_products.models import Tag
from eshop_product_category.models import Category
from eshop_brand.models import Brand


# Create your views here.
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):
        return Product.objects.get_active()


class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(url=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')

        return Product.objects.get_product_by_category(category.id)


def products_detail(request, *args, **kwargs):
    product_name = kwargs['name']
    product_id = kwargs['productId']
    product = Product.objects.get_by_id(product_id)
    if product is None or not product.is_active:
        raise Http404()

    tag = product.Tag.all()
    gallery = Gallery.objects.filter(product_id=product_id).all()
    category = Category.objects.all()
    gallery = list(my_grouper(3, gallery))
    context = {
        'product': product,
        'tag': tag,
        'category': category,
        'gallery': gallery
    }

    return render(request, 'products/product-details.html', context)


class SearchProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active()


def product_brand(request, *args, **kwargs):
    brand = Brand.objects.all()
    context = {
        'brand': brand
    }
    return render(request, 'products/product_brand_partial.html', context)


class ProductBrandList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 12

    def get_queryset(self):

        brand_url = self.kwargs['brand_url']
        brand = Brand.objects.filter(url=brand_url).first()
        if brand is not None:
            product = Product.objects.filter(Brand_id=brand.id).all()
        else:
            raise Http404('محصولی با انی برند ثبت نشده')
        return product


def product_suggestion(request, *args, **kwargs):
    product_id = kwargs['productId']
    product_all_category = Product.objects.filter(id=product_id).first().category.all()
    all_product = Product.objects.all().values('id')
    all_product_id = list(map(lambda x: x['id'], all_product))
    all_product_relationship_category = Product.objects.filter(category__in=all_product_id).distinct()[:9]
    sug1 = []
    sug2 = []
    suggestion = list(my_grouper(3, all_product_relationship_category))
    print(suggestion)
    temp = 1
    for item in all_product_relationship_category:
        if temp <= 3:
            sug1.append(item)
            temp += 1
        else:
            sug2.append(item)

    context = {
        'suggestion': suggestion,
        'sug1': sug1,
        'sug2': sug2,
    }
    return render(request, 'products/product_suggestion_partial.html', context)
