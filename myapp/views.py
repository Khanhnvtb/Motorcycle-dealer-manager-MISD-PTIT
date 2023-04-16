from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory

from .forms import *
from .models import *


# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home.html', {'user': user})
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.ERROR, 'Tài khoản hoặc mật khẩu không chính xác')
    else:
        username = ''
        password = ''
    return render(request, "login.html", {'username': username, 'password': password})


def logoutUser(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, "Đăng xuất thành công")
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def addUser(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Tài khoản đã tồn tại')
            else:
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                user_form = UserForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm người dùng thành công')
    else:
        user_form = UserForm()
    return render(request, 'add_user.html', {'user_form': user_form})


@login_required(login_url='/login/')
def updateUser(request, username):
    user = User.objects.filter(username=username).first()
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin người dùng thành công', )
    else:
        user_form = UserForm(instance=user)
    return render(request, 'update_user.html', {'user_form': user_form, 'username': username})


@login_required(login_url='/login/')
def deleteUser(request, username):
    user = User.objects.filter(username=username).first()
    user.delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, 'Xoá người dùng thành công')
    users = User.objects.all()
    return render(request, 'user_manager.html', {'users': users})


@login_required(login_url='/login/')
def addMotor(request):
    if request.method == "POST":
        motor_form = MotorForm(request.POST, request.FILES)
        if motor_form.is_valid():
            if Motor.objects.filter(name=motor_form.cleaned_data['name']).exists():
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Xe đã tồn tại')
            else:
                motor_form.save()
                motor_form = MotorForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm xe thành công')
    else:
        motor_form = MotorForm()
    return render(request, 'add_motor.html', {'motor_form': motor_form})


@login_required(login_url='/login/')
def updateMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id).first()
    if request.method == "POST":
        motor_form = MotorForm(request.POST, instance=motor)
        if motor_form.is_valid():
            motor_form.save()
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin xe thành công')
    else:
        motor_form = MotorForm(instance=motor)
    return render(request, 'update_motor.html', {'motor_form': motor_form, 'motor_id': motor_id})


@login_required(login_url='/login/')
def deleteMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id).first()
    motor.delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, 'Xoá xe thành công')
    motors = Motor.objects.all()
    return render(request, 'motor_manager.html', {'motors': motors})


@login_required(login_url='/login/')
def addStore(request):
    if request.method == "POST":
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            if Store.objects.filter(name=store_form.cleaned_data['name']).exists():
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Cửa hàng đã tồn tại')
            else:
                store_form.save()
                store_form = StoreForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm cửa hàng thành công')
    else:
        store_form = StoreForm()
    return render(request, 'add_store.html', {'store_form': store_form})


@login_required(login_url='/login/')
def updateStore(request, store_id):
    store = Store.objects.filter(store_id=store_id).first()
    if request.method == "POST":
        store_form = StoreForm(request.POST, instance=store)
        if store_form.is_valid():
            store_form.save()
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin cửa hàng thành công', )
    else:
        store_form = StoreForm(instance=store)
    return render(request, 'update_store.html', {'store_form': store_form, 'store_id': store_id})


@login_required(login_url='/login/')
def deleteStore(request, store_id):
    store = Store.objects.filter(store_id=store_id).first()
    store.delete()
    stores = Store.objects.all()
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, 'Xóa cửa hàng thành công', )
    return render(request, 'store_manager.html', {'stores': stores})


@login_required(login_url='/login/')
def addSupplier(request):
    if request.method == "POST":
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            if Supplier.objects.filter(name=supplier_form.cleaned_data['name']).exists():
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Nhà cung cấp đã tồn tại')
            else:
                supplier_form.save()
                supplier_form = SupplierForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm nhà cung cấp thành công')
    else:
        supplier_form = SupplierForm()
    return render(request, 'add_supplier.html', {'supplier_form': supplier_form})


@login_required(login_url='/login/')
def updateSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
    if request.method == "POST":
        supplier_form = SupplierForm(request.POST, instance=supplier)
        if supplier_form.is_valid():
            supplier_form.save()
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin nhà cung cấp thành công', )
    else:
        supplier_form = SupplierForm(instance=supplier)
    return render(request, 'update_supplier.html', {'supplier_form': supplier_form, 'supplier_id': supplier_id})


@login_required(login_url='/login/')
def deleteSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
    supplier.delete()
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, 'Xoá nhà cung cấp thành công')
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_manager.html', {'suppliers': suppliers})


@login_required(login_url='/login/')
def userManager(request):
    users = User.objects.all()
    return render(request, 'user_manager.html', {'users': users})


@login_required(login_url='/login/')
def storeManager(request):
    stores = Store.objects.all()
    return render(request, 'store_manager.html', {'stores': stores})


@login_required(login_url='/login/')
def motorManager(request):
    motors = Motor.objects.all()
    return render(request, 'motor_manager.html', {'motors': motors})


@login_required(login_url='/login/')
def supplierManager(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_manager.html', {'suppliers': suppliers})


@login_required(login_url='/login/')
def showUser(request):
    user = request.user
    return render(request, 'show_user.html', {'user': user})


@login_required(login_url='/login/')
def showUser(request, username):
    user = User.objects.filter(username=username).first()
    return render(request, 'show_user.html', {'user': user})


@login_required(login_url='/login/')
def showMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id).first()
    return render(request, 'show_motor.html', {'motor': motor})


@login_required(login_url='/login/')
def showSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
    return render(request, 'show_supplier.html', {'supplier': supplier})


@login_required(login_url='/login/')
def showStore(request, store_id):
    store = Store.objects.filter(store_id=store_id).first()
    return render(request, 'show_store.html', {'store': store})


@login_required(login_url='/login/')
def formset_view(request):
    context = {}

    # creating a formset and 5 instances of ImportForm
    ImportFormSet = formset_factory(ImportForm, extra=5)
    import_forms = ImportFormSet(request.POST or None)

    # print formset data if it is valid
    if import_forms.is_valid():
        for import_form in import_forms:
            employee = request.user
            motor = import_form.cleaned_data.get('motor')
            supplier = import_form.cleaned_data.get('supplier')
            quantity = import_form.cleaned_data.get('quantity')
            if motor and supplier and quantity:
                motor.quantity += quantity
                motor.save()
                import_invoice = Import_Invoice(total=quantity * motor.import_price,
                                                employee_id=employee.id,
                                                supplier_id=supplier.supplier_id)
                import_invoice.save()
                import_motor = Import_Motor(invoice_id=import_invoice.invoice_id,
                                            motor_id=motor.motor_id,
                                            quantity=quantity)
                import_motor.save()
            else:
                pass
            storage = messages.get_messages(request)
            storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Nhập hàng thàng công')
        import_forms = ImportFormSet()
    context['import_forms'] = import_forms
    return render(request, "import_motor.html", context)
