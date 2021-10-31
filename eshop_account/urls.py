from django.urls import path
from .views import login, account, register

urlpatterns = [
    path('', account, name='account'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]
