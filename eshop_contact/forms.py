from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی راوارد کنید', 'class': 'form-control'}),
        label='نام و نام خانوادگی'

    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form-control'}),
        label='ایمیل',

    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان پیام', 'class': 'form-control'}),
        label='عنوان پیام'

    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام را وارد کنید'}),
        label='متن پیام'

    )

