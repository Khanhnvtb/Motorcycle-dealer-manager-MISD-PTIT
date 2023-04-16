from django import forms
from django.utils.datetime_safe import datetime
from django.core.validators import MinValueValidator
from .models import *

gender_choice = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Khác', 'Khác'),
]

role_choice = [
    ('Nhân viên bán hàng', 'Nhân viên bán hàng'),
    ('Nhân viên kho', 'Nhân viên kho'),
]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'username'}),
            'password': forms.PasswordInput(attrs={'class': 'password'}),
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nguyễn Văn A'}),
            'avatar': forms.FileInput(attrs={'class': 'avatar'}),
            'dob': forms.TextInput(attrs={'class': 'dob', 'placeholder': '2001-01-01'}),
            'gender': forms.Select(choices=gender_choice),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
            'role': forms.Select(choices=role_choice),
            'salary': forms.TextInput(attrs={'class': 'salary'}),
            'is_superuser': forms.TextInput(attrs={'value': 0}),
            'first_name': forms.TextInput(attrs={'value': ''}),
            'last_name': forms.TextInput(attrs={'value': ''}),
            'is_staff': forms.TextInput(attrs={'value': 0}),
            'is_active': forms.TextInput(attrs={'value': 1}),
            'date_joined': forms.TextInput(attrs={'value': datetime.now()}),
        }


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"
        widgets = {
            'motor_id': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'brand': forms.TextInput(attrs={'class': 'brand'}),
            'image': forms.FileInput(attrs={'class': 'image'}),
            'description': forms.TextInput(attrs={'class': 'description'}),
            'assurance': forms.TextInput(attrs={'class': 'assurance'}),
            'quantity': forms.TextInput(attrs={'value': 0}),
            'import_price': forms.TextInput(attrs={'class': 'import_price'}),
            'export_price': forms.TextInput(attrs={'class': 'export_price'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        widgets = {
            'supplier_id': forms.TextInput(),
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
            'store_id': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': 'name'}),
            'owner': forms.TextInput(attrs={'class': 'owner'}),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
        }


class ImportFromSupplierFrom(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), label='Nhà cung cấp',
                                      help_text='Chọn một nhà cung cấp từ danh sách',
                                      error_messages={
                                          'required': 'Bạn phải chọn một nhà cung cấp'})


class ImportForm(forms.Form):
    motor = forms.ModelChoiceField(queryset=Motor.objects.all(), label='Xe máy',
                                   help_text='Chọn một xe máy từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một xe máy'
                                   })
    quantity = forms.IntegerField(validators=[MinValueValidator(1)], label='Số lượng',
                                  help_text='Nhập số lượng xe máy cần nhập',
                                  error_messages={
                                      'required': 'Bạn phải nhập số lượng',
                                      'invalid': 'Số lượng phải là một số nguyên',
                                      'min_value': 'Số lượng phải lớn hơn hoặc bằng 1',
                                  })


class ExportToStoreForm(forms.Form):
    store = forms.ModelChoiceField(queryset=Store.objects.all(), label='Cửa hàng',
                                   help_text='Chọn một nhà cửa hàng từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một cửa hàng'})


class ExportForm(forms.Form):
    motor = forms.ModelChoiceField(queryset=Motor.objects.all(), label='Xe máy',
                                   help_text='Chọn một xe máy từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một xe máy'
                                   })
    quantity = forms.IntegerField(validators=[MinValueValidator(1)], label='Số lượng',
                                  help_text='Nhập số lượng xe máy cần nhập',
                                  error_messages={
                                      'required': 'Bạn phải nhập số lượng',
                                      'invalid': 'Số lượng phải là một số nguyên',
                                      'min_value': 'Số lượng phải lớn hơn hoặc bằng 1',
                                  })
