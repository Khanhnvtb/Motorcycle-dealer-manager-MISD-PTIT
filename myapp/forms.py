from django import forms
from .models import *

gender_choice = ['Nam', 'Nữ', 'Khác']
role_choice = ['Nhân viên bán hàng', 'Nhân viên kho']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'username'}),
            'password': forms.TextInput(attrs={'class': 'password', 'placeholder': 'password'}),
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nguyễn Văn A'}),
            'avatar': forms.TextInput(attrs={'class': 'avatar'}),
            'dob': forms.TextInput(attrs={'class': 'dob', 'placeholder': '2001-01-01'}),
            'gender': forms.TextInput(attrs={'class': 'gender'}),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
            'role': forms.TextInput(attrs={'class': 'role'}),
        }


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'brand': forms.TextInput(attrs={'class': 'brand'}),
            'image': forms.TextInput(attrs={'class': 'image'}),
            'description': forms.TextInput(attrs={'class': 'description'}),
            'assurance': forms.TextInput(attrs={'class': 'assurance'}),
            'quantity': forms.TextInput(attrs={'class': 'quantity'}),
            'import_price': forms.TextInput(attrs={'class': 'import_price'}),
            'export_price': forms.TextInput(attrs={'class': 'export_price'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'owner': forms.TextInput(attrs={'class': 'owner'}),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
        }
