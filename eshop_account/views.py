from django.shortcuts import render


# Create your views here.

def account(request):
    context = {}
    return render(request=request, template_name='account/LoginOrRegister.html', context=context)


def login(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='account/shared/_Login.html', context=context)


def register(request, *args, **kwargs):
    context = {}
    return render(request=request, template_name='account/shared/_Register.html', context=context)
