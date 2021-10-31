from django.urls import path
from .views import  login_user, register_user

app_name = "eshop_account"
urlpatterns = [
    # path('', account, name='home'),
    path('login', login_user, name='login'),
    path('register', register_user, name='register')
]
