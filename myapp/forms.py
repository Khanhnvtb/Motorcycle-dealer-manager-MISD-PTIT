from django import forms
from django.utils.datetime_safe import datetime
from django.core.validators import MinValueValidator

from .models import *
from datetime import date

gender_choice = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Khác', 'Khác'),
]

role_choice = [
    ('Nhân viên bán hàng', 'Nhân viên bán hàng'),
    ('Nhân viên kho', 'Nhân viên kho'),
]

month_choice = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
    ('11', 11),
    ('12', 12),
]


def get_year_choices():
    year_choice = []
    curr_year = datetime.today().year
    for i in range(curr_year, -1, -1):
        year_choice.append(tuple([i, i]))
    return year_choice


month_choice = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
    ('11', 11),
    ('12', 12),
]


def get_year_choices():
    year_choice = []
    curr_year = datetime.today().year
    for i in range(curr_year, -1, -1):
        year_choice.append(tuple([i, i]))
    return year_choice


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'avatar', 'dob', 'gender', 'address', 'phone', 'email', 'role',
                  'salary']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username form-control', 'placeholder': 'Tài khoản'}),
            'password': forms.PasswordInput(
                attrs={'class': 'password form-control', 'placeholder': 'Mật khẩu', 'type': 'password'}),
            'name': forms.TextInput(attrs={'class': 'name form-control', 'placeholder': 'Nguyễn Văn A'}),
            'avatar': forms.FileInput(attrs={'class': 'avatar form-control', 'type': 'file'}),
            'dob': forms.DateInput(attrs={'class': 'dob form-control', 'type': 'date'}),
            'gender': forms.Select(choices=gender_choice, attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'address form-control'}),
            'phone': forms.TextInput(attrs={'class': 'phone form-control'}),
            'email': forms.EmailInput(attrs={'class': 'email form-control', 'type': 'email'}),
            'role': forms.Select(choices=role_choice, attrs={'class': 'form-select'}),
            'salary': forms.TextInput(attrs={'class': 'salary form-control', 'type': 'number'}),
        }
        labels = {
            'username': 'Tài khoản',
            'password': 'Mật khẩu',
            'name': 'Họ và tên',
            'avatar': 'Ảnh',
            'dob': 'Ngày sinh',
            'gender': 'Giới tính',
            'address': 'Địa chỉ',
            'phone': 'Số điện thoại',
            'email': 'Email',
            'role': 'Chức vụ',
            'salary': 'Lương',
        }


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = "__all__"
        widgets = {
            'motor_id': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': 'name form-control'}, ),
            'brand': forms.TextInput(attrs={'class': 'brand form-control'}),
            'image': forms.FileInput(attrs={'class': 'image form-control', 'type': 'file'}),
            'description': forms.Textarea(attrs={'class': 'description form-control', 'rows': 5}),
            'assurance': forms.TextInput(attrs={'class': 'assurance form-control'}),
            'quantity': forms.TextInput(attrs={'value': 0, 'class': 'quantity form-control', 'type': 'hidden'}),
            'import_price': forms.TextInput(attrs={'class': 'import_price form-control', 'type': 'number'}),
            'export_price': forms.TextInput(attrs={'class': 'export_price form-control', 'type': 'number'}),
        }
        labels = {
            'motor_id': 'Motor ID',
            'name': 'Tên xe',
            'brand': 'Hãng xe',
            'image': 'Ảnh',
            'description': 'Mô tả',
            'assurance': 'Bảo hành',
            'quantity': 'Số lượng',
            'import_price': 'Giá nhập',
            'export_price': 'Giá bán',
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        widgets = {
            'supplier_id': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': 'name form-control'}, ),
            'address': forms.TextInput(attrs={'class': 'address form-control'}),
            'phone': forms.TextInput(attrs={'class': 'phone form-control'}),
            'email': forms.TextInput(attrs={'class': 'email form-control', 'type': 'email'}),
            'transport_price': forms.TextInput(attrs={'class': 'transport_price form-control', 'type': 'number'}),
            'delivery_day': forms.TextInput(attrs={'class': 'delivery_day form-control', 'type': 'number'}),
            'rating': forms.TextInput(attrs={'class': 'rating form-control', 'type': 'number'}),
        }
        labels = {
            'supplier_id': 'Supplier ID',
            'name': 'Tên nhà cung cấp',
            'address': 'Địa chỉ',
            'phone': 'Số điện thoại',
            'email': 'Email',
            'transport_price': 'Phí vận chuyển',
            'delivery_day': 'Thời gian giao hàng',
            'rating': 'Đánh giá chất lượng',
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"
        widgets = {
            'store_id': forms.TextInput(),
            'name': forms.TextInput(attrs={'class': 'name form-control'}, ),
            'owner': forms.TextInput(attrs={'class': 'owner form-control'}),
            'address': forms.TextInput(attrs={'class': 'address form-control'}),
            'phone': forms.TextInput(attrs={'class': 'phone form-control'}),
            'email': forms.TextInput(attrs={'class': 'email form-control', 'type': 'email'}),
        }
        labels = {
            'store_id': 'Store ID',
            'name': 'Tên cửa hàng',
            'owner': 'Tên chủ cửa hàng',
            'address': 'Địa chỉ',
            'phone': 'Số điện thoại',
            'email': 'Email',
        }


class ImportFromSupplierFrom(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), label='Nhà cung cấp',
                                      help_text='Chọn một nhà cung cấp từ danh sách',
                                      error_messages={
                                          'required': 'Bạn phải chọn một nhà cung cấp'},
                                      widget=forms.Select(attrs={'class': 'form-select'}))


class ImportForm(forms.Form):
    motor = forms.ModelChoiceField(queryset=Motor.objects.all(), label='Xe máy',
                                   help_text='Chọn một xe máy từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một xe máy'
                                   },
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    quantity = forms.IntegerField(validators=[MinValueValidator(1)], label='Số lượng',
                                  help_text='Nhập số lượng xe máy cần nhập',
                                  error_messages={
                                      'required': 'Bạn phải nhập số lượng',
                                      'invalid': 'Số lượng phải là một số nguyên',
                                      'min_value': 'Số lượng phải lớn hơn hoặc bằng 1',
                                  },
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                'placeholder': 'Nhập vào số lượng'}))


class ExportToStoreForm(forms.Form):
    store = forms.ModelChoiceField(queryset=Store.objects.all(), label='Cửa hàng',
                                   help_text='Chọn một nhà cửa hàng từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một cửa hàng'},
                                   widget=forms.Select(attrs={'class': 'form-select'}))


class ExportForm(forms.Form):
    motor = forms.ModelChoiceField(queryset=Motor.objects.all(), label='Xe máy',
                                   help_text='Chọn một xe máy từ danh sách',
                                   error_messages={
                                       'required': 'Bạn phải chọn một xe máy'
                                       ,
                                   },
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    quantity = forms.IntegerField(validators=[MinValueValidator(1)], label='Số lượng',
                                  help_text='Nhập số lượng xe máy cần nhập',
                                  error_messages={
                                      'required': 'Bạn phải nhập số lượng',
                                      'invalid': 'Số lượng phải là một số nguyên',
                                      'min_value': 'Số lượng phải lớn hơn hoặc bằng 1',
                                  },
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                'placeholder': 'Nhập vào số lượng'}))


class DateForm(forms.Form):
    start_month = forms.ChoiceField(choices=month_choice, label='Tháng: ',
                                    help_text='Chọn một tháng từ danh sách',
                                    widget=forms.Select(attrs={'class': 'form-select'}))
    start_year = forms.ChoiceField(choices=[], label='Năm: ', help_text='Chọn một năm từ danh sách',
                                   widget=forms.Select(attrs={'class': 'form-select'}))
    end_month = forms.ChoiceField(choices=month_choice, label='Tháng: ',
                                  help_text='Chọn một tháng từ danh sách',
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    end_year = forms.ChoiceField(choices=[], label='Năm: ', help_text='Chọn một năm từ danh sách',
                                 widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super(DateForm, self).__init__(*args, **kwargs)
        # gọi hàm get_year_choices và gán kết quả cho choices
        self.fields['start_year'].choices = get_year_choices()
        self.fields['end_year'].choices = get_year_choices()


class MonthForm(forms.Form):
    month = forms.ChoiceField(choices=month_choice, label='Tháng: ', help_text='Chọn một tháng từ danh sách',
                              widget=forms.Select(attrs={'class': 'form-select'}))
    year = forms.ChoiceField(choices=[], label='Năm: ', help_text='Chọn một năm từ danh sách',
                             widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super(MonthForm, self).__init__(*args, **kwargs)
        # gọi hàm get_year_choices và gán kết quả cho choices
        self.fields['year'].choices = get_year_choices()


class DebtForm(forms.Form):
    debt_term = forms.DateField(validators=[MinValueValidator(date.today())], label='Ngày hết hạn: ',
                                help_text='Chọn ngày hết hạn',
                                error_messages={
                                    'required': 'Bạn phải nhập vào một ngày',
                                    'invalid': 'Bạn phải nhập theo định dạng ngày',
                                    'min_value': 'Không được nhập ngày nhỏ hơn hôm nay',
                                },
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))


class ImportReceiptForm(forms.Form):
    money = forms.IntegerField(validators=[MinValueValidator(1)], label='Số tiền: ',
                               error_messages={
                                   'required': 'Bạn phải nhập vào số tiền',
                                   'invalid': 'Bạn phải nhập giá trị là số nguyên',
                                   'min_value': 'Không được nhập nhỏ hơn 1'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                             'placeholder': 'Nhập vào số tiền'}))
    note = forms.CharField(label='Ghi chú: ', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))


class ExportReceiptForm(forms.Form):
    money = forms.IntegerField(validators=[MinValueValidator(1)], label='Số tiền: ',
                               error_messages={
                                   'required': 'Bạn phải nhập vào số tiền',
                                   'invalid': 'Bạn phải nhập giá trị là số nguyên',
                                   'min_value': 'Không được nhập nhỏ hơn 1'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                             'placeholder': 'Nhập vào số tiền'}))
    note = forms.CharField(label='Ghi chú: ', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))


class ExpenseForm(forms.Form):
    money = forms.IntegerField(validators=[MinValueValidator(1)], label='Số tiền: ',
                               error_messages={
                                   'required': 'Bạn phải nhập vào số tiền',
                                   'invalid': 'Bạn phải nhập giá trị là số nguyên',
                                   'min_value': 'Không được nhập nhỏ hơn 1'},
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                             'placeholder': 'Nhập vào số tiền'}))
    type = forms.CharField(label='Loại chi phí: ',
                           error_messages={
                               'required': 'Bạn phải nhập chuỗi ký tự',
                           },
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nhập vào loại chi phí'}))
    note = forms.CharField(label='Ghi chú: ', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
