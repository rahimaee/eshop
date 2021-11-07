from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView


class NewsList(ListView):
    template_name = ''
    paginate_by = 12
