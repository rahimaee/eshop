from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='نام کاربری'

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'name': 'password', 'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='رمز عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if is_exists_user is False:
            raise forms.ValidationError('کاربر پیدا نشد')
        return user_name

    def clean_password(self):
        if len(self.cleaned_data.get('password')) < 4:
            raise forms.ValidationError("sad")
        return self.cleaned_data.get('password')


class RegisterForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید',}),
        label='ایمیل',

    )
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='نام کاربری'

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='رمز عبور'
    )
    password_config = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        label='رمز عبور'
    )

    def clean_password_config(self):
        password = self.cleaned_data.get('password')
        password_config = self.cleaned_data.get('password_config')
        if not password == password_config:
            raise forms.ValidationError('رمز عبور با تکرار ان برار نیست')
        return password_config

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('کاربری با این نام وجود دارد')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('کاربری با این ایمیل وجود دارد')
        return email
