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
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'username'}),
            'password': forms.PasswordInput(attrs={'class': 'password'}),
            'name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Nguyễn Văn A'}),
            'avatar': forms.FileInput(attrs={'class': 'avatar'}),
            'dob': forms.DateInput(attrs={'class': 'dob', 'placeholder': '2001-01-01'}),
            'gender': forms.Select(choices=gender_choice),
            'address': forms.TextInput(attrs={'class': 'address'}),
            'phone': forms.TextInput(attrs={'class': 'phone'}),
            'email': forms.EmailInput(attrs={'class': 'email'}),
            'role': forms.Select(choices=role_choice),
            'salary': forms.TextInput(attrs={'class': 'salary'}),
            'is_superuser': forms.HiddenInput(attrs={'value': 0}),
            'first_name': forms.HiddenInput(attrs={'value': ''}),
            'last_name': forms.HiddenInput(attrs={'value': ''}),
            'is_staff': forms.HiddenInput(attrs={'value': 1}),
            'is_active': forms.HiddenInput(attrs={'value': 1}),
            'date_joined': forms.HiddenInput(attrs={'value': datetime.now()}),
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
            'transport_price': forms.TextInput(attrs={'class': 'transport_price'}),
            'delivery_day': forms.TextInput(attrs={'class': 'delivery_day'}),
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


class DateForm(forms.Form):
    start_month = forms.ChoiceField(choices=month_choice, label='Tháng bắt đầu: ',
                                    help_text='Chọn một tháng từ danh sách', )
    start_year = forms.ChoiceField(choices=[], label='Năm bắt đầu: ', help_text='Chọn một năm từ danh sách', )
    end_month = forms.ChoiceField(choices=month_choice, label='Tháng kết thúc: ',
                                  help_text='Chọn một tháng từ danh sách', )
    end_year = forms.ChoiceField(choices=[], label='Năm kết thúc: ', help_text='Chọn một năm từ danh sách', )   
    def __init__(self, *args, **kwargs):
        super(DateForm, self).__init__(*args, **kwargs)
        # gọi hàm get_year_choices và gán kết quả cho choices
        self.fields['start_year'].choices = get_year_choices()
        self.fields['end_year'].choices = get_year_choices()


class MonthForm(forms.Form):
    month = forms.ChoiceField(choices=month_choice, label='Tháng: ', help_text='Chọn một tháng từ danh sách', )
    year = forms.ChoiceField(choices=[], label='Năm: ', help_text='Chọn một năm từ danh sách', )

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
                                })


class ImportReceiptForm(forms.Form):
    import_invoice = forms.ModelChoiceField(queryset=Import_Invoice.objects.all(), label='Đơn nhập',
                                     help_text='Chọn một nhà đơn nhập từ danh sách',
                                     error_messages={
                                         'required': 'Bạn phải chọn đơn nhập'})
    money = forms.IntegerField(label='Số tiền: ', help_text='Nhập vào số tiền',
                               error_messages={
                                   'required': 'Bạn phải nhập vào số tiền',
                                   'invalid': 'Bạn phải nhập giá trị là số nguyên', })
    note = forms.CharField(label='Ghi chú: ', required=False)


class ExportReceiptForm(forms.Form):
    delivery_invoice = forms.ModelChoiceField(queryset=Delivery_Invoice.objects.all(), label='Đơn nhập',
                                            help_text='Chọn một nhà đơn nhập từ danh sách',
                                            error_messages={
                                                'required': 'Bạn phải chọn đơn nhập'})
    money = forms.IntegerField(label='Số tiền: ', help_text='Nhập vào số tiền',
                               error_messages={
                                   'required': 'Bạn phải nhập vào số tiền',
                                   'invalid': 'Bạn phải nhập giá trị là số nguyên', })
    note = forms.CharField(label='Ghi chú: ', required=False)
