from django import forms
from django.utils.datetime_safe import datetime

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
            'password': forms.TextInput(attrs={'class': 'password', 'type': 'password'}),
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nguyễn Văn A'}),
            'avatar': forms.TextInput(attrs={'class': 'avatar'}),
            'dob': forms.TextInput(attrs={'class': 'dob', 'placeholder': '2001-01-01'}),
            'gender': forms.Select(choices=gender_choice),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'email'}),
            'role': forms.Select(choices=role_choice),
            'is_superuser': forms.TextInput(attrs={'value': 0}),
            'first_name': forms.TextInput(attrs={'value': ''}),
            'last_name': forms.TextInput(attrs={'value': ''}),
            'is_staff': forms.TextInput(attrs={'value': 0}),
            'is_active': forms.TextInput(attrs={'value': 1}),
            'date_joined': forms.TextInput(attrs={'value': datetime.now()}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['salary']
        widgets = {
            'salary': forms.TextInput(attrs={'class': 'salary'}),
        }


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"
        widgets = {
            'motor_id': forms.TextInput(),
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


class ImportForm(forms.Form):
    motor = forms.ModelChoiceField(queryset=Motor.objects.all())
    quantity = forms.IntegerField()
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    total = forms.DecimalField(disabled=True)

    def clean(self):
        # gọi phương thức clean() của lớp cha
        cleaned_data = super().clean()
        # lấy ra quantity và motor từ form
        quantity = cleaned_data.get("quantity")
        motor = cleaned_data.get("motor")
        # kiểm tra nếu cả hai đều có giá trị
        if quantity and motor:
            # lấy ra import_price của motor từ cơ sở dữ liệu
            import_price = Motor.objects.get(motor_id=motor.motor_id).import_price
            # tính toán total bằng cách nhân quantity với import_price
            total = quantity * import_price
            # gán total vào cleaned_data
            cleaned_data["total"] = total
        # trả về cleaned_data
        return cleaned_data
