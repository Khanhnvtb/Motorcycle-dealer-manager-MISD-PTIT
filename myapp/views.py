from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
            messages.add_message(request, messages.ERROR, 'Tài khoản hoặc mật khẩu không chính xác')
    else:
        username = ''
        password = ''
    return render(request, "login.html", {'username': username, 'password': password})


def logoutUser(request):
    logout(request)
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
                messages.add_message(request, messages.SUCCESS, 'Tài khoản đã tồn tại')
            else:
                user_form.save()
                user_form = UserForm()
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
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin người dùng thành công', )
    else:
        user_form = UserForm(instance=user)
    return render(request, 'update_user.html', {'user_form': user_form, 'username': username})


@login_required(login_url='/login/')
def deleteUser(request, username):
    user = User.objects.filter(username=username).first()
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Xoá người dùng thành công')
    users = User.objects.all()
    return render(request, 'user_manager.html', {'users': users})


@login_required(login_url='/login/')
def addMotor(request):
    if request.method == "POST":
        motor_form = MotorForm(request.POST)
        if motor_form.is_valid():
            if Motor.objects.filter(name=motor_form.cleaned_data['name']).exists():
                messages.add_message(request, messages.ERROR, 'Xe đã tồn tại')
            else:
                motor_form.save()
                motor_form = MotorForm()
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
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin xe thành công')
    else:
        motor_form = MotorForm(instance=motor)
    return render(request, 'update_motor.html', {'motor_form': motor_form, 'motor_id': motor_id})


@login_required(login_url='/login/')
def deleteMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id).first()
    motor.delete()
    messages.add_message(request, messages.SUCCESS, 'Xoá xe thành công')
    motors = Motor.objects.all()
    return render(request, 'motor_manager.html', {'motors': motors})


@login_required(login_url='/login/')
def addStore(request):
    if request.method == "POST":
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            if Store.objects.filter(name=store_form.cleaned_data['name']).exists():
                messages.add_message(request, messages.ERROR, 'Cửa hàng đã tồn tại')
            else:
                store_form.save()
                store_form = StoreForm()
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
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin cửa hàng thành công', )
    else:
        store_form = StoreForm(instance=store)
    return render(request, 'update_store.html', {'store_form': store_form, 'store_id': store_id})


@login_required(login_url='/login/')
def deleteStore(request, store_id):
    store = Store.objects.filter(store_id=store_id).first()
    store.delete()
    stores = Store.objects.all()
    messages.add_message(request, messages.SUCCESS, 'Xóa cửa hàng thành công', )
    return render(request, 'store_manager.html', {'stores': stores})


@login_required(login_url='/login/')
def addSupplier(request):
    if request.method == "POST":
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            if Supplier.objects.filter(name=supplier_form.cleaned_data['name']).exists():
                messages.add_message(request, messages.ERROR, 'Nhà cung cấp đã tồn tại')
            else:
                supplier_form.save()
                supplier_form = SupplierForm()
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
            messages.add_message(request, messages.SUCCESS, 'Sửa thông tin nhà cung cấp thành công', )
    else:
        supplier_form = SupplierForm(instance=supplier)
    return render(request, 'update_supplier.html', {'supplier_form': supplier_form, 'supplier_id': supplier_id})


@login_required(login_url='/login/')
def deleteSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
    supplier.delete()
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
    employee = Employee.objects.filter(employee_id=user.id).first()
    return render(request, 'show_user.html', {'user': user, 'employee': employee})


@login_required(login_url='/login/')
def showUser(request, username):
    user = User.objects.filter(username=username).first()
    employee = Employee.objects.filter(employee_id=user.id).first()
    return render(request, 'show_user.html', {'user': user, 'employee': employee})


@login_required(login_url='/login/')
def showMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id)
    return render(request, 'show_motor.html', {'motor': motor})


@login_required(login_url='/login/')
def showSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id)
    return render(request, 'show_supplier.html', {'supplier': supplier})


@login_required(login_url='/login/')
def showStore(request, store_id):
    store = Store.objects.filter(store_id=store_id)
    return render(request, 'show_store.html', {'store': store})


@login_required(login_url='/login/')
def importMotor(request):
    if request.method == "POST":
        import_form = ImportForm(request.POST)
        if import_form.is_valid():
            employee = request.user
            import_invoice = Import_Invoice(total=0,
                                            # total=import_form.cleaned_data['total'],
                                            employee_id=employee.user_id,
                                            supplier_id=import_form.cleaned_data['supplier'].supplier_id)
            import_invoice.save()
            import_motor = Import_Motor(invoice_id=import_invoice.invoice_id,
                                        motor_id=import_form.cleaned_data['motor'].motor_id,
                                        quantity=import_form.cleaned_data['quantity'])
            import_motor.save()
            motor = import_form.cleaned_data['motor']
            motor.quantity += import_form.cleaned_data['quantity']
            motor.save()
            messages.add_message(request, messages.SUCCESS, 'Nhập hàng thàng công')

    else:
        import_form = ImportForm()
    return render(request, 'import_motor.html', {'import_form': import_form})
