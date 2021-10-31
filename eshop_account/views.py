from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.models import User


# Create your views here.


# def account(request):
#
#
# login and register in  one view
# if request.user.is_authenticated:
#     return redirect('starting_page')
# login_form = LoginForm(request.POST == "login_form" or None)
# register_form = RegisterForm(request.POST == "register_form" or None)
# context = {
#     'login_form': login_form,
#     'register_form': register_form
# }
# if "login_form" in request.POST:
#     if login_form.is_valid():
#         user_name = login_form.cleaned_data.get('user_name')
#         password = login_form.cleaned_data.get('password')
#         user = authenticate(request, username=user_name, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('starting_page')
#         else:
#             login_form.add_error('user_name', 'کاربری یافت نشد')
#
# if "register_form" in request.POST:
#     if register_form.is_valid():
#         user_name = register_form.cleaned_data.get('user_name')
#         password = register_form.cleaned_data.get('password')
#         email = register_form.cleaned_data.get('email')
#         User.objects.create_user(username=user_name, password=password, email=email)
#         return redirect('starting_page')
#
# return render(request=request, template_name='account/LoginOrRegister.html', context=context)
#

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('starting_page')
    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('account:login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)
