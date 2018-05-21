from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Profile

class UserRegister(forms.ModelForm):
    password = forms.CharField(label='Mật khẩu',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Nhập lại mật khẩu',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email',)
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Mật khẩu không khớp')
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        user_name = []
        for u in User.objects.all():
            user_name.append(u.username)
        if username in user_name:
            raise forms.ValidationError('Tài khoản này đã tồn tại')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        emails = []
        for u in User.objects.all():
            emails.append(u.email)
        if email in emails:
            raise forms.ValidationError('Email này đã tồn tại')
        return email

