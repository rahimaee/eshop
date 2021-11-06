from django.shortcuts import render, redirect
from eshop_order.forms import UserNewOrderForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from eshop_order.models import Order
from eshop_products.models import Product


@login_required(login_url='account/login')
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
            print(request.user.id)

        product_id = new_order_form.cleaned_data.get('productId')
        product = Product.objects.get_by_id(product_id=product_id)
        count = new_order_form.cleaned_data.get('count')
        order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        return redirect('/')
