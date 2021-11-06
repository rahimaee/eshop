from django.urls import path
from .views import contact_page

app_name = 'eshop_contact'

urlpatterns = [
    path('', contact_page, name='page'),
]
