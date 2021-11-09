from django.http import HttpResponse
from django.shortcuts import render, redirect
from eshop_order.forms import UserNewOrderForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from eshop_order.models import Order
from eshop_products.models import Product
import requests
import json


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
        up = order.orderdetail_set.filter(product_id=product_id).first()

        if up is not None:
            up.count += count
            up.price = product.price
            up.save()
        else:
            order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        return redirect('/')


@login_required(login_url='account/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None,
    }

    user_id = request.user.id
    all_order_detail = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    all_order_detail = all_order_detail.orderdetail_set.all()
    for pro in all_order_detail:
        if pro is not None:
            pro.price = Product.objects.filter(pk=pro.product.pk).first().price
            pro.save()
    open_order = Order.objects.filter(owner_id=user_id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
    return render(request, 'order/user_open_order.html', context)


MERCHANT = 'ae558394-741d-11e7-b007-000c295eb8fc'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.

CallbackURL = 'http://127.0.0.1:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
