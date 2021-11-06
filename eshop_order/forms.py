from django import forms
from django.contrib.auth.models import User


class UserNewOrderForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )
