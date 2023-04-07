from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
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
        user_form = UserForm(request.POST)
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


@login_required(login_url='/login')
def addMotor(request):
    if request.method == "POST":
        motor_form = MotorForm(request.POST)
        if motor_form.is_valid():
            try:
                Motor.objects.get(name=motor_form.cleaned_data['name'])
                messages.add_message(request, messages.ERROR, 'Xe đã tồn tại')
            except Motor.DoesNotExist:
                motor_form.save()
                motor_form = MotorForm()
                messages.add_message(request, messages.SUCCESS, 'Thêm xe thành công')
    else:
        motor_form = MotorForm()
    return render(request, 'add_motor.html', {'motor_form': motor_form})


@login_required(login_url='/login')
def addStore(request):
    if request.method == "POST":
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            try:
                Store.objects.get(name=store_form.cleaned_data['name'])
                messages.add_message(request, messages.ERROR, 'Cửa hàng đã tồn tại')
            except Motor.DoesNotExist:
                store_form.save()
                store_form = StoreForm()
                messages.add_message(request, messages.SUCCESS, 'Thêm cửa hàng thành công')
    else:
        store_form = StoreForm()
    return render(request, 'add_store.html', {'store_form': store_form})


@login_required(login_url='/login')
def addSupplier(request):
    if request.method == "POST":
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            try:
                Supplier.objects.get(name=supplier_form.cleaned_data['name'])
                messages.add_message(request, messages.ERROR, 'Nhà cung cấp đã tồn tại')
            except Motor.DoesNotExist:
                supplier_form.save()
                supplier_form = SupplierForm()
                messages.add_message(request, messages.SUCCESS, 'Thêm nhà cung cấp thành công')
    else:
        supplier_form = SupplierForm()
    return render(request, 'add_supplier.html', {'store_form': supplier_form})


@login_required(login_url='/login')
def userManager(request):
    users = User.objects.all()
    return render(request, 'user_manager.html', {'users': users})


@login_required(login_url='/login')
def storeManager(request):
    stores = Store.objects.all()
    return render(request, 'store_manager.html', {'stores': stores})


@login_required(login_url='/login')
def motorManager(request):
    motors = Motor.objects.all()
    return render(request, 'motor_manager.html', {'motors': motors})


@login_required(login_url='/login')
def supplierManager(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_manager.html', {'suppliers': suppliers})


@login_required(login_url='/login')
def showUser(request):
    user = request.user
    # employee = Employee.objects.get(employee_id=user.objects.username)
    return render(request, 'show_user.html', {'user': user})
    # return render(request, 'show_user.html', {'user': user}, {'employee': employee}

@login_required(login_url='/login')
def showMotor(request, motor_id):
    motor = Motor.objects.filter(motor_id=motor_id)
    return render(request, 'show_motor.html', {'motor': motor})


@login_required(login_url='/login')
def showSupplier(request, supplier_id):
    supplier = Supplier.objects.filter(supplier_id=supplier_id)
    return render(request, 'show_supplier.html', {'supplier': supplier})


@login_required(login_url='/login')
def showStore(request, store_id):
    store = Store.objects.filter(store_id=store_id)
    return render(request, 'show_store.html', {'store': store})
