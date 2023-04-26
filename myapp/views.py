from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import formset_factory
import os
from .forms import *
from .models import *
from datetime import date
from django.db import connection
from django.core.paginator import Paginator
import calendar
import joblib
import pandas as pd
# import sklearn


# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.ERROR, 'Tài khoản hoặc mật khẩu không chính xác')
    else:
        username = ''
        password = ''
    return render(request, "login.html", {'username': username, 'password': password})


@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, "Đăng xuất thành công")
    return redirect('/login/')


def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def addUser(request):
    if request.user.role == 'admin':
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                user_form = UserForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm người dùng thành công')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Tài khoản đã có người sử dụng')
        else:
            user_form = UserForm()
    else:
        return render(request, 'home.html')
    return render(request, 'add_user.html', {'user_form': user_form})


@login_required(login_url='/login/')
def updateUser(request, username):
    if request.user.role == 'admin':
        user = User.objects.filter(username=username).first()
        if request.method == "POST":
            user_form = UserForm(request.POST, instance=user)
            if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Sửa thông tin người dùng thành công', )
        else:
            user_form = UserForm(instance=user)
    else:
        render(request, 'home.html')
    return render(request, 'update_user.html', {'user_form': user_form, 'username': username})


@login_required(login_url='/login/')
def deleteUser(request, username):
    if request.user.role == 'admin':
        user = User.objects.filter(username=username).first()
        user.delete()
        os.remove(f"myapp/static/media/{user.avatar}")
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Xoá người dùng thành công')
        users = User.objects.all()
        paginator = Paginator(users, 10)  # Show 10 contacts per page.

        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
    else:
        return render(request, 'home.html')
    return render(request, 'user_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def addMotor(request):
    if request.user.role != 'Nhân viên bán hàng':
        if request.method == "POST":
            motor_form = MotorForm(request.POST, request.FILES)
            if motor_form.is_valid():
                motor_form.save()
                motor_form = MotorForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm xe thành công')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Xe đã tồn tại trong hệ thống')
        else:
            motor_form = MotorForm()
    else:
        return render(request, 'home.html')
    return render(request, 'add_motor.html', {'motor_form': motor_form})


@login_required(login_url='/login/')
def updateMotor(request, motor_id):
    if request.user.role != 'Nhân viên bán hàng':
        motor = Motor.objects.filter(motor_id=motor_id).first()
        if request.method == "POST":
            motor_form = MotorForm(request.POST, instance=motor)
            if motor_form.is_valid():
                motor_form.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Sửa thông tin xe thành công')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Xe đã tồn tại trong hệ thống')
        else:
            motor_form = MotorForm(instance=motor)
    else:
        return render(request, 'home.html')
    return render(request, 'update_motor.html', {'motor_form': motor_form, 'motor_id': motor_id})


@login_required(login_url='/login/')
def deleteMotor(request, motor_id):
    if request.user.role != 'Nhân viên bán hàng':
        motor = Motor.objects.filter(motor_id=motor_id).first()
        motor.delete()
        os.remove(f"myapp/static/media/{motor.image}")
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Xoá xe thành công')
        motors = Motor.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(motors, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'motor_manager.html', {"page_obj": page_obj})


@login_required(login_url='/login/')
def addStore(request):
    if request.user.role != "Nhân viên kho":
        if request.method == "POST":
            store_form = StoreForm(request.POST)
            if store_form.is_valid():
                store_form.save()
                store_form = StoreForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm cửa hàng thành công')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Cửa hàng đã tồn tại trong hệ thống')
        else:
            store_form = StoreForm()
    else:
        return render(request, 'home.html')
    return render(request, 'add_store.html', {'store_form': store_form})


@login_required(login_url='/login/')
def updateStore(request, store_id):
    if request.user.role != "Nhân viên kho":
        store = Store.objects.filter(store_id=store_id).first()
        if request.method == "POST":
            store_form = StoreForm(request.POST, instance=store)
            if store_form.is_valid():
                store_form.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Sửa thông tin cửa hàng thành công', )
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Cửa hàng đã tồn tại trong hệ thống')
        else:
            store_form = StoreForm(instance=store)
    else:
        return render(request, 'home.html')
    return render(request, 'update_store.html', {'store_form': store_form, 'store_id': store_id})


@login_required(login_url='/login/')
def deleteStore(request, store_id):
    if request.user.role != "Nhân viên kho":
        store = Store.objects.filter(store_id=store_id).first()
        store.delete()
        stores = Store.objects.all()
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Xóa cửa hàng thành công', )
    else:
        return render(request, 'home.html')
    paginator = Paginator(stores, 10)  # Show 20 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'store_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def addSupplier(request):
    if request.user.role != 'Nhân viên bán hàng':
        if request.method == "POST":
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                supplier_form = SupplierForm()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thêm nhà cung cấp thành công')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Nhà cung cấp đã tồn tại trong hệ thống')
        else:
            supplier_form = SupplierForm()
    else:
        return render(request, 'home.html')
    return render(request, 'add_supplier.html', {'supplier_form': supplier_form})


@login_required(login_url='/login/')
def updateSupplier(request, supplier_id):
    if request.user.role != 'Nhân viên bán hàng':
        supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
        if request.method == "POST":
            supplier_form = SupplierForm(request.POST, instance=supplier)
            if supplier_form.is_valid():
                supplier_form.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Sửa thông tin nhà cung cấp thành công', )
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Nhà cung cấp đã tồn tại trong hệ thống')
        else:
            supplier_form = SupplierForm(instance=supplier)
    else:
        return render(request, 'home.html')
    return render(request, 'update_supplier.html', {'supplier_form': supplier_form, 'supplier_id': supplier_id})


@login_required(login_url='/login/')
def deleteSupplier(request, supplier_id):
    if request.user.role != 'Nhân viên bán hàng':
        supplier = Supplier.objects.filter(supplier_id=supplier_id).first()
        supplier.delete()
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Xoá nhà cung cấp thành công')
        suppliers = Supplier.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(suppliers, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'supplier_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def userManager(request):
    context = {}
    if request.user.role == "admin":
        keyword = request.GET.get('keyword', None)
        if keyword:
            users = User.objects.filter(name__contains=keyword)
            context['keyword'] = keyword
        else:
            users = User.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(users, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'user_manager.html', context)


@login_required(login_url='/login/')
def storeManager(request):
    context = {}
    if request.user.role != "Nhân viên kho":
        keyword = request.GET.get('keyword', None)
        if keyword:
            stores = Store.objects.filter(name__contains=keyword)
            context['keyword'] = keyword
        else:
            stores = Store.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(stores, 10)  # Show 20 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'store_manager.html', context)


@login_required(login_url='/login/')
def motorManager(request):
    context = {}
    if request.user.role != 'Nhân viên bán hàng':
        keyword = request.GET.get('keyword', None)
        if keyword:
            motors = Motor.objects.filter(name__contains=keyword)
            context['keyword'] = keyword
        else:
            motors = Motor.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(motors, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'motor_manager.html', context)


@login_required(login_url='/login/')
def supplierManager(request):
    if request.user.role != "Nhân viên bán hàng":
        if request.method == "POST":
            keyword = request.POST.get('keyword', None)
            suppliers = Supplier.objects.filter(name__contains=keyword)
        else:
            suppliers = Supplier.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(suppliers, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'supplier_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def showUser(request):
    user = request.user
    return render(request, 'show_user.html', {'user': user})


@login_required(login_url='/login/')
def showUser(request, username):
    if request.user.role == 'admin':
        user = User.objects.filter(username=username).first()
    else:
        return render(request, 'home.html')
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
def importMotor(request):
    if request.user.role == 'Nhân viên kho':
        context = {}

        # creating a formset and 5 instances of ImportForm
        ImportFormSet = formset_factory(ImportForm, extra=5)
        import_forms = ImportFormSet(request.POST or None)
        supplier_form = ImportFromSupplierFrom(request.POST or None)
        debt_form = DebtForm(request.POST or None)
        if supplier_form.is_valid() and debt_form.is_valid() and import_forms.is_valid():
            supplier = supplier_form.cleaned_data['supplier']
            debt_term = debt_form.cleaned_data['debt_term']
            total = 0
            import_dict = {}
            for import_form in import_forms:
                motor = import_form.cleaned_data.get('motor')
                quantity = import_form.cleaned_data.get('quantity')
                if motor and quantity:
                    total += quantity * motor.import_price
                    if motor in import_dict.keys():
                        import_dict[motor] += quantity
                    else:
                        import_dict[motor] = quantity
            if total == 0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Bạn chưa chọn các sản phẩm cần nhập')
            else:
                import_invoice = Import_Invoice(total=total, employee_id=request.user.id,
                                                supplier_id=supplier.supplier_id,
                                                debt_term=debt_term)
                import_invoice.save()
                for motor in import_dict.keys():
                    quantity = import_dict[motor]
                    motor.quantity += quantity
                    motor.save()
                    import_motor = Import_Motor(invoice_id=import_invoice.invoice_id,
                                                motor_id=motor.motor_id,
                                                quantity=quantity)
                    import_motor.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Nhập hàng thàng công')
                import_forms = ImportFormSet()

        context['import_forms'] = import_forms
        context['supplier_form'] = supplier_form
        context['debt_form'] = debt_form
    else:
        return render(request, 'home.html')
    return render(request, "import_motor.html", context)


@login_required(login_url='/login/')
def exportMotor(request):
    if request.user.role == 'Nhân viên bán hàng':
        context = {}

        # creating a formset and 5 instances of ExportForm
        ExportFormSet = formset_factory(ExportForm, extra=5)
        export_forms = ExportFormSet(request.POST or None)
        store_form = ExportToStoreForm(request.POST or None)
        debt_form = DebtForm(request.POST or None)
        if store_form.is_valid() and debt_form.is_valid() and export_forms.is_valid():
            store = store_form.cleaned_data['store']
            debt_term = debt_form.cleaned_data['debt_term']
            total = 0
            export_dict = {}
            for export_form in export_forms:
                motor = export_form.cleaned_data.get('motor')
                quantity = export_form.cleaned_data.get('quantity')
                if motor and quantity:
                    total += quantity * motor.export_price
                    if motor in export_dict.keys():
                        export_dict[motor] += quantity
                    else:
                        export_dict[motor] = quantity
            if total == 0:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Bạn chưa chọn các sản phẩm cần xuất')
            else:  # nếu đã viết
                for motor in export_dict.keys():
                    quantity = export_dict[motor]
                    if motor.quantity < quantity:
                        storage = messages.get_messages(request)
                        storage.used = True
                        messages.add_message(request, messages.ERROR,
                                             f'Số lượng {motor} trong kho chỉ còn {motor.quantity}')
                        context['export_forms'] = export_forms
                        context['store_form'] = store_form
                        return render(request, "export_motor.html", context)
                delivery_invoice = Delivery_Invoice(total=total,
                                                    employee_id=request.user.id,
                                                    store_id=store.store_id, debt_term=debt_term)
                delivery_invoice.save()
                for motor in export_dict.keys():
                    quantity = export_dict[motor]
                    motor.quantity -= quantity
                    motor.save()
                    delivery_motor = Delivery_Motor(invoice_id=delivery_invoice.invoice_id,
                                                    motor_id=motor.motor_id,
                                                    quantity=quantity)
                    delivery_motor.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Xuất hàng thàng công')
                export_forms = ExportFormSet()
                store_form = ExportToStoreForm()

        context['export_forms'] = export_forms
        context['store_form'] = store_form
        context['debt_form'] = debt_form
    else:
        return render(request, 'home.html')
    return render(request, "export_motor.html", context)


@login_required(login_url='/login/')
def reportView(request, username):
    return render(request, 'report.html', {'username': username})


def getStartDate(year, month):
    return date(year, month, 1)


def getEndDate(year, month):
    return date(year, month, calendar.monthrange(year, month)[1])


# admin
@login_required(login_url='/login/')
def reportBalanceSheet(request):
    if request.user.role == 'admin':
        results = ()
        if request.method == "GET":
            date_form = DateForm(request.GET)
            if date_form.is_valid():
                start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                          int(date_form.cleaned_data['start_month']))
                end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
                if start_date > end_date:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_delivery_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    results = []
                    # lấy ra kết quả bằng phương thức fetchall()
                    for record in cursor.fetchall():
                        results.append(list(record))

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_import_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    i = 0
                    for record in cursor.fetchall():
                        results[i].append(record[1])
                        i += 1

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(money) " \
                            "from myapp_expense " \
                            "where time between '{s2}' and '{s3}' " \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    i = 0
                    for record in cursor.fetchall():
                        results[i][2] += record[1]
                        i += 1

                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            date_form = DateForm()
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 12)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'report_turnover.html', {'date_form': date_form, 'page_obj': page_obj})


# admin, bán hàng
@login_required(login_url='/login/')
def reportSaleItems(request):
    report = {}
    if request.user.role != 'Nhân viên kho':
        if request.method == "GET":
            date_form = DateForm(request.GET)
            if date_form.is_valid():
                start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                          int(date_form.cleaned_data['start_month']))
                end_date = getEndDate(int(date_form.cleaned_data['end_year']),
                                      int(date_form.cleaned_data['end_month']))
                if start_date > end_date:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "SELECT date_format(Time, '{s1}') as Month_sale, " \
                            "myapp_Motor.image, myapp_Motor.name, SUM(myapp_Delivery_Motor.quantity) AS quantity " \
                            "FROM myapp_Motor " \
                            "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.motor_Id " \
                            "JOIN myapp_delivery_invoice ON myapp_delivery_motor.invoice_id = myapp_delivery_invoice.invoice_id " \
                            "WHERE myapp_delivery_invoice.time between '{s2}' AND '{s3}' " \
                            "GROUP BY Month_sale, myapp_Motor.name, myapp_Motor.Image " \
                            "ORDER BY Month_sale, quantity".format(s1="%Y-%m",
                                                                   s2=str(start_date),
                                                                   s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    # lấy ra kết quả bằng phương thức fetchall()
                    results = cursor.fetchall()
                    for record in results:
                        key = record[0]
                        if key not in report.keys():
                            report[key] = [tuple([record[1], record[2], record[3]])]
                        else:
                            report[key].append(tuple([record[1], record[2], record[3]]))
                    report = [(k, v) for k, v in report.items()]
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            date_form = DateForm()
    else:
        return render(request, 'home.html')
    paginator = Paginator(list(report), 2)  # Show 2 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'report_sale_items.html', {'date_form': date_form, 'page_obj': page_obj})


# admin, bán hàng
@login_required(login_url='/login/')
def reportBestSaleItems(request):
    if request.user.role != 'Nhân viên kho':
        year = datetime.now().year
        month = datetime.now().month
        start_date = getStartDate(year, month)
        end_date = getEndDate(year, month)

        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()

        query = "SELECT myapp_Motor.motor_id, myapp_Motor.image, myapp_Motor.name " \
                "FROM myapp_Motor " \
                "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.motor_Id " \
                "JOIN myapp_Delivery_Invoice ON myapp_Delivery_Motor.invoice_Id = myapp_Delivery_Invoice.invoice_Id " \
                "WHERE myapp_Delivery_Invoice.time between '{s1}' and '{s2}'" \
                "GROUP BY myapp_Motor.name, myapp_Motor.image " \
                "ORDER BY SUM(myapp_Delivery_Motor.quantity) " \
                "DESC LIMIT 5".format(s1=str(start_date), s2=str(end_date))

        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Thành công')
        paginator = Paginator(results, 10)  # Show 10 contacts per page.

        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
    else:
        return render(request, 'home.html')
    return render(request, 'report_best_sale_items.html', {'page_obj': page_obj})


# admin, bán hàng trùng username
@login_required(login_url='/login/')
def saleHistory(request, username):
    if request.user.role == 'admin' or (
            request.user.role == 'Nhân viên bán hàng' and request.user.username == username):
        name = User.objects.filter(username=username).first().name
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()

        query = "SELECT date_format(myapp_Delivery_invoice.time, '{s1}') AS time, myapp_Motor.motor_Id, myapp_Motor.name, " \
                "myapp_Motor.image, myapp_Store.name, myapp_Store.store_Id, myapp_Delivery_motor.quantity " \
                "FROM myapp_Motor " \
                "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.Motor_Id " \
                "JOIN myapp_Delivery_Invoice ON myapp_Delivery_Motor.Invoice_Id = myapp_Delivery_Invoice.invoice_Id " \
                "JOIN myapp_User ON myapp_Delivery_Invoice.Employee_Id = myapp_User.Id " \
                "JOIN myapp_Store ON myapp_Delivery_Invoice.Store_Id = myapp_Store.store_Id " \
                "WHERE myapp_User.username = '{s2}' " \
                "ORDER BY time DESC".format(s1="%d-%m-%Y %T", s2=username)
        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'sale_history.html', {'page_obj': page_obj, 'name': name})


# admin
@login_required(login_url='/login/')
def reportSaleHistory(request):
    if request.user.role == 'admin':
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()

        query = "SELECT date_format(myapp_Delivery_invoice.time, '{s1}') AS time, myapp_Motor.motor_Id, myapp_User.username, " \
                "myapp_User.name, myapp_Motor.name, myapp_Motor.image, myapp_Store.name, myapp_Store.Store_Id, " \
                "myapp_Delivery_motor.quantity " \
                "FROM myapp_Motor " \
                "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.Motor_Id " \
                "JOIN myapp_Delivery_Invoice ON myapp_Delivery_Motor.Invoice_Id = myapp_Delivery_Invoice.invoice_Id " \
                "JOIN myapp_User ON myapp_Delivery_Invoice.Employee_Id = myapp_User.Id " \
                "JOIN myapp_Store ON myapp_Delivery_Invoice.Store_Id = myapp_Store.Store_Id " \
                "ORDER BY time DESC".format(s1="%d-%m-%Y %T")

        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'report_sale_history.html', {'page_obj': page_obj})


# admin, kho trùng username
@login_required(login_url='/login/')
def importHistory(request, username):
    if request.user.role == 'admin' or (request.user.role == 'Nhân viên kho' and request.user.username == username):
        name = User.objects.filter(username=username).first().name
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(myapp_IMPORT_INVOICE.TIME,'{s1}') AS TIME, myapp_MOTOR.MOTOR_ID, myapp_MOTOR.NAME, " \
                "myapp_MOTOR.IMAGE, myapp_SUPPLIER.NAME, myapp_SUPPLIER.SUPPLIER_ID, myapp_IMPORT_MOTOR.QUANTITY " \
                "FROM myapp_MOTOR " \
                "JOIN myapp_IMPORT_MOTOR ON myapp_MOTOR.MOTOR_ID = myapp_IMPORT_MOTOR.MOTOR_ID " \
                "JOIN myapp_IMPORT_INVOICE ON myapp_IMPORT_MOTOR.INVOICE_ID = myapp_IMPORT_INVOICE.INVOICE_ID " \
                "JOIN myapp_USER ON myapp_IMPORT_INVOICE.EMPLOYEE_ID = myapp_USER.ID " \
                "JOIN myapp_SUPPLIER ON myapp_IMPORT_INVOICE.SUPPLIER_ID = myapp_SUPPLIER.SUPPLIER_ID " \
                "WHERE myapp_user.USERNAME = '{s2}' " \
                "ORDER BY TIME DESC".format(s1="%d-%m-%Y %T", s2=username)
        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'import_history.html', {'page_obj': page_obj, 'name': name})


# admin
@login_required(login_url='/login/')
def reportImportHistory(request):
    if request.user.role == 'admin':
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(myapp_IMPORT_INVOICE.TIME,'{s1}') AS TIME , myapp_USER.NAME, myapp_User.Username, " \
                "myapp_MOTOR.MOTOR_Id, myapp_MOTOR.NAME, myapp_MOTOR.IMAGE, myapp_SUPPLIER.NAME, " \
                "myapp_SUPPLIER.SUPPLIER_ID, myapp_IMPORT_MOTOR.QUANTITY " \
                "FROM myapp_MOTOR " \
                "JOIN myapp_IMPORT_MOTOR " \
                "ON myapp_MOTOR.MOTOR_ID = myapp_IMPORT_MOTOR.MOTOR_ID " \
                "JOIN myapp_IMPORT_INVOICE " \
                "ON myapp_IMPORT_MOTOR.INVOICE_ID = myapp_IMPORT_INVOICE.INVOICE_ID " \
                "JOIN myapp_USER " \
                "ON myapp_IMPORT_INVOICE.EMPLOYEE_ID = myapp_USER.ID " \
                "JOIN myapp_SUPPLIER " \
                "ON myapp_IMPORT_INVOICE.SUPPLIER_ID = myapp_SUPPLIER.SUPPLIER_ID " \
                "ORDER BY TIME DESC".format(s1="%d-%m-%Y %T")

        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()
        storage = messages.get_messages(request)
        storage.used = True
        messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'report_import_history.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def visualization(request, username):
    return render(request, 'visualization.html', {'username': username})


# admin
@login_required(login_url='/login/')
def visualizationBalanceSheet(request):
    if request.user.role == 'admin':
        columns_name = []
        one_values = []
        two_values = []
        if request.method == "POST":
            date_form = DateForm(request.POST)
            if date_form.is_valid():
                start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                          int(date_form.cleaned_data['start_month']))
                end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
                if start_date > end_date:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_delivery_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    # lấy ra kết quả bằng phương thức fetchall()
                    results = cursor.fetchall()

                    for record in results:
                        columns_name.append(record[0])
                        one_values.append(int(record[1]))
        
                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_import_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    for record in cursor.fetchall():
                        two_values.append(int(record[1]))

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(money) " \
                            "from myapp_expense " \
                            "where time between '{s2}' and '{s3}' " \
                            "group by Month_sale " \
                            "order by Month_sale".format(s1="%Y-%m",
                                                         s2=str(start_date),
                                                         s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    i = 0
                    for record in cursor.fetchall():
                        two_values[i] += int(record[1])
                        i += 1

                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            date_form = DateForm()
    else:
        return render(request, 'home.html')
    return render(request, 'visualization_turnover.html',
                  {'date_form': date_form, 'columns_name': columns_name, 'one_values': one_values,
                   'two_values': two_values})


# admin, bán hàng
@login_required(login_url='/login/')
def visualizationSaleItems(request):
    columns_name = []
    values = []
    if request.method == "POST":
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                      int(date_form.cleaned_data['start_month']))
            end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
            if start_date > end_date:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.ERROR, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
            else:
                # tạo một con trỏ cho cơ sở dữ liệu
                cursor = connection.cursor()

                query = "SELECT myapp_Motor.name, SUM(myapp_Delivery_Motor.quantity) AS quantity " \
                        "FROM myapp_Motor " \
                        "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.motor_Id " \
                        "JOIN myapp_delivery_invoice ON myapp_delivery_motor.invoice_id = myapp_delivery_invoice.invoice_id " \
                        "WHERE myapp_delivery_invoice.time between '{s1}' AND '{s2}' " \
                        "GROUP BY myapp_Motor.name " \
                        "ORDER BY quantity DESC".format(s1=str(start_date), s2=str(end_date))

                # chạy câu lệnh SQL bằng phương thức execute()
                cursor.execute(query)

                # lấy ra kết quả bằng phương thức fetchall()
                results = cursor.fetchall()

                for record in results:
                    columns_name.append(record[0])
                    values.append(int(record[1]))

                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        date_form = DateForm()
    return render(request, 'visualization_sale_items.html',
                  {'date_form': date_form, 'columns_name': columns_name, 'values': values})


# admin, bán hàng
@login_required(login_url='/login/')
def visualizationBestSaleItems(request):
    columns_name = []
    values = []

    year = datetime.now().year
    month = datetime.now().month
    start_date = getStartDate(year, month)
    end_date = getEndDate(year, month)

    # tạo một con trỏ cho cơ sở dữ liệu
    cursor = connection.cursor()

    query = "SELECT myapp_Motor.name, SUM(myapp_Delivery_Motor.quantity) AS quantity " \
            "FROM myapp_Motor " \
            "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.motor_Id " \
            "JOIN myapp_Delivery_Invoice ON myapp_Delivery_Motor.invoice_Id = myapp_Delivery_Invoice.invoice_Id " \
            "WHERE myapp_Delivery_Invoice.time between '{s1}' and '{s2}'" \
            "GROUP BY myapp_Motor.name " \
            "ORDER BY quantity " \
            "DESC LIMIT 5".format(s1=str(start_date), s2=str(end_date))

    # chạy câu lệnh SQL bằng phương thức execute()
    cursor.execute(query)

    # lấy ra kết quả bằng phương thức fetchall()
    results = cursor.fetchall()

    for record in results:
        columns_name.append(record[0])
        values.append(int(record[1]))

    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.SUCCESS, 'Thành công')
    return render(request, 'visualization_best_sale_items.html', {'columns_name': columns_name, 'values': values})


# admin, bán hàng trùng username
@login_required(login_url='/login/')
def visualizationKpiUser(request, username):
    if request.user.role == 'admin' or (
            request.user.role == 'Nhân viên bán hàng' and request.user.username == username):
        user = User.objects.filter(username=username).first()
        columns_name = []
        values = []
        if request.method == "POST":
            date_form = DateForm(request.POST)
            if date_form.is_valid():
                start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                          int(date_form.cleaned_data['start_month']))
                end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
                if start_date > end_date:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "SELECT date_format(time, '{s1}') AS Month_sale, SUM(total) as sales " \
                            "FROM myapp_delivery_invoice " \
                            "WHERE myapp_delivery_invoice.employee_id = {s2} " \
                            "AND myapp_delivery_invoice.time BETWEEN '{s3}' AND '{s4}' " \
                            "GROUP BY Month_sale " \
                            "ORDER BY Month_sale DESC".format(s1="%Y-%m", s2=user.id, s3=str(start_date),
                                                              s4=str(end_date))

                    print(query)
                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    # lấy ra kết quả bằng phương thức fetchall()
                    results = cursor.fetchall()

                    for record in results:
                        columns_name.append(record[0])
                        values.append(int(record[1]))

                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            date_form = DateForm()
    else:
        return render(request, 'home.html')
    return render(request, 'visualization_kpi_user.html', {'date_form': date_form,
                                                           'username': username, 'name': user.name,
                                                           'columns_name': columns_name, 'values': values})


# admin
@login_required(login_url='/login/')
def visualizationKpi(request):
    if request.user.role == 'admin':
        columns_name = []
        values = []

        if request.method == "POST":
            month_form = MonthForm(request.POST)
            if month_form.is_valid():
                start_date = getStartDate(int(month_form.cleaned_data['year']), int(month_form.cleaned_data['month']))
                end_date = getEndDate(int(month_form.cleaned_data['year']), int(month_form.cleaned_data['month']))

            # tạo một con trỏ cho cơ sở dữ liệu
            cursor = connection.cursor()

            query = "SELECT myapp_user.name as name, SUM(total) as sales " \
                    "FROM myapp_delivery_invoice " \
                    "JOIN myapp_user ON myapp_delivery_invoice.employee_id = myapp_user.id " \
                    "WHERE myapp_delivery_invoice.time BETWEEN '{s1}' AND '{s2}' " \
                    "GROUP BY name " \
                    "ORDER BY sales DESC".format(s1=str(start_date), s2=str(end_date))

            # chạy câu lệnh SQL bằng phương thức execute()
            cursor.execute(query)

            # lấy ra kết quả bằng phương thức fetchall()
            results = cursor.fetchall()

            for record in results:
                columns_name.append(record[0])
                values.append(int(record[1]))
        else:
            month_form = MonthForm()
    else:
        return render(request, 'home.html')
    return render(request, 'visualization_kpi.html',
                  {'month_form': month_form, 'columns_name': columns_name, 'values': values})


# admin, kho
@login_required(login_url='/login/')
def visualizationImportFromSupplier(request):
    columns_name = []
    values = []
    # tạo một con trỏ cho cơ sở dữ liệu
    cursor = connection.cursor()

    query = "select myapp_supplier.name as name, sum(myapp_import_motor.quantity) as quantity " \
            "from myapp_supplier " \
            "join myapp_import_invoice on myapp_supplier.supplier_id = myapp_import_invoice.supplier_id " \
            "join myapp_import_motor on myapp_import_invoice.invoice_id = myapp_import_motor.invoice_id " \
            "group by name " \
            "order by quantity DESC"

    # chạy câu lệnh SQL bằng phương thức execute()
    cursor.execute(query)

    # lấy ra kết quả bằng phương thức fetchall()
    results = cursor.fetchall()

    for record in results:
        columns_name.append(record[0])
        values.append(int(record[1]))

    return render(request, 'visualization_import_from_supplier.html', {'columns_name': columns_name, 'values': values})


# admin, bán hàng
@login_required(login_url='/login/')
def visualizationExportToStore(request):
    columns_name = []
    values = []
    # tạo một con trỏ cho cơ sở dữ liệu
    cursor = connection.cursor()

    query = "select myapp_store.name as name, sum(myapp_delivery_motor.quantity) as quantity " \
            "from myapp_store " \
            "join myapp_delivery_invoice on myapp_store.store_id = myapp_delivery_invoice.store_id " \
            "join myapp_delivery_motor on myapp_delivery_invoice.invoice_id = myapp_delivery_motor.invoice_id " \
            "group by name " \
            "order by quantity DESC"

    # chạy câu lệnh SQL bằng phương thức execute()
    cursor.execute(query)

    # lấy ra kết quả bằng phương thức fetchall()
    results = cursor.fetchall()

    for record in results:
        columns_name.append(record[0])
        values.append(int(record[1]))

    return render(request, 'visualization_export_to_store.html', {'columns_name': columns_name, 'values': values})


# kho
@login_required(login_url='/login/')
def importReceipt(request, invoice_id):
    if request.user.role == "Nhân viên kho":
        if request.method == "POST":
            import_form = ImportReceiptForm(request.POST)
            if import_form.is_valid():
                employee_id = request.user.id
                import_invoice = Import_Invoice.objects.get(invoice_id=invoice_id)
                time = date.today()
                money = import_form.cleaned_data.get('money')
                note = import_form.cleaned_data.get('note')
                max_money = import_invoice.total - import_invoice.payment
                if money > max_money:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, f'Số tiền không được lớn hơn {max_money}')
                    return render(request, 'import_receipt.html', {'import_receipt_form': import_form})
                else:
                    import_receipt = ImportReceipt(employee_id=employee_id, invoice_id=import_invoice.invoice_id,
                                                   time=time, money=money, note=note)
                    import_receipt.save()
                    import_invoice.payment += money
                    import_invoice.save()
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thanh toán thành công')
                    import_form = ImportReceiptForm()
        else:
            import_form = ImportReceiptForm()
    else:
        return render(request, 'home.html')
    return render(request, 'import_receipt.html', {'import_receipt_form': import_form, 'invoice_id': invoice_id})


# bán hàng
@login_required(login_url='/login/')
def exportReceipt(request, invoice_id):
    if request.user.role == "Nhân viên bán hàng":
        if request.method == "POST":
            export_form = ExportReceiptForm(request.POST)
            if export_form.is_valid():
                employee_id = request.user.id
                export_invoice = Delivery_Invoice.objects.get(invoice_id=invoice_id)
                time = date.today()
                money = export_form.cleaned_data.get('money')
                note = export_form.cleaned_data.get('note')
                max_money = export_invoice.total - export_invoice.payment
                if money > max_money:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.ERROR, f'Số tiền không được lớn hơn {max_money}')
                    return render(request, 'export_receipt.html', {'export_receipt_form': export_form})
                else:
                    delivery_receipt = DeliveryReceipt(employee_id=employee_id, invoice_id=export_invoice.invoice_id,
                                                       time=time, money=money, note=note)
                    delivery_receipt.save()
                    export_invoice.payment += money
                    export_invoice.save()
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thanh toán thành công')
                    export_form = ExportReceiptForm()
        else:
            export_form = ExportReceiptForm()
    else:
        return render(request, 'home.html')
    return render(request, 'export_receipt.html', {'export_receipt_form': export_form, 'invoice_id': invoice_id})


@login_required(login_url='/login/')
def invoiceManager(request):
    context = {}
    if request.user.role == "Nhân viên bán hàng":
        keyword = request.GET.get('keyword', None)
        if keyword:
            invoices = Delivery_Invoice.objects.filter(invoice_id__contains=keyword).extra(
                select={'balance': 'total - payment'}).order_by('-balance')
            context['keyword'] = keyword
        else:
            invoices = Delivery_Invoice.objects.extra(select={'balance': 'total - payment'}).order_by('-balance')
    elif request.user.role == "Nhân viên kho":
        keyword = request.GET.get('keyword', None)
        if keyword:
            invoices = Import_Invoice.objects.filter(invoice_id__contains=keyword).extra(
                select={'balance': 'total - payment'}).order_by('-balance')
            context['keyword'] = keyword
        else:
            invoices = Import_Invoice.objects.extra(select={'balance': 'total - payment'}).order_by('-balance')
    else:
        return render(request, 'home.html')
    paginator = Paginator(invoices, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'invoice_manager.html', context)


@login_required(login_url='/login/')
def showInvoice(request, invoice_id):
    if request.user.role != 'admin':
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()
        if request.user.role == 'Nhân viên bán hàng':
            invoice = Delivery_Invoice.objects.get(invoice_id=invoice_id)
            query = "select myapp_motor.name, myapp_delivery_motor.quantity " \
                    "from myapp_motor " \
                    "join myapp_delivery_motor on myapp_delivery_motor.motor_id = myapp_motor.motor_id " \
                    "where myapp_delivery_motor.invoice_id = {s1}".format(s1=invoice_id)
            customer = Store.objects.get(store_id=invoice.store_id)
        else:
            invoice = Import_Invoice.objects.get(invoice_id=invoice_id)
            query = "select myapp_motor.name, myapp_import_motor.quantity " \
                    "from myapp_motor " \
                    "join myapp_import_motor on myapp_import_motor.motor_id = myapp_motor.motor_id " \
                    "where myapp_import_motor.invoice_id = {s1}".format(s1=invoice_id)
            customer = Supplier.objects.get(supplier_id=invoice.supplier_id)
        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        name = User.objects.get(id=invoice.employee_id).name
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'show_invoice.html',
                  {'page_obj': page_obj, 'invoice': invoice, 'name': name, 'customer': customer})


@login_required(login_url='/login/')
def receiptHistory(request, invoice_id):
    if request.user.role != 'admin':
        # tạo một con trỏ cho cơ sở dữ liệu
        cursor = connection.cursor()
        if request.user.role == 'Nhân viên bán hàng':
            invoice = Delivery_Invoice.objects.get(invoice_id=invoice_id)
            query = "select myapp_deliveryreceipt.time, myapp_deliveryreceipt.money, myapp_deliveryreceipt.note, " \
                    "myapp_user.name " \
                    "from myapp_delivery_invoice " \
                    "join myapp_deliveryreceipt on myapp_delivery_invoice.invoice_id = myapp_deliveryreceipt.invoice_id " \
                    "join myapp_user on myapp_deliveryreceipt.employee_id = myapp_user.id " \
                    "where myapp_delivery_invoice.invoice_id = {s1}".format(s1=invoice_id)
            customer = Store.objects.get(store_id=invoice.store_id)
        else:
            invoice = Import_Invoice.objects.get(invoice_id=invoice_id)
            query = "select myapp_importreceipt.time, myapp_importreceipt.money, myapp_importreceipt.note, " \
                    "myapp_user.name " \
                    "from myapp_import_invoice " \
                    "join myapp_importreceipt on myapp_import_invoice.invoice_id = myapp_importreceipt.invoice_id " \
                    "join myapp_user on myapp_importreceipt.employee_id = myapp_user.id " \
                    "where myapp_import_invoice.invoice_id = {s1}".format(s1=invoice_id)
            customer = Supplier.objects.get(supplier_id=invoice.supplier_id)
        # chạy câu lệnh SQL bằng phương thức execute()
        cursor.execute(query)

        # lấy ra kết quả bằng phương thức fetchall()
        results = cursor.fetchall()

        name = User.objects.get(id=invoice.employee_id).name
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'receipt_history.html',
                  {'page_obj': page_obj, 'invoice': invoice, 'name': name, 'customer': customer})


@login_required(login_url='/login/')
def expenseManager(request):
    if request.user.role == "Nhân viên bán hàng":
        if request.method == "POST":
            keyword = request.POST.get('keyword', None)
            expense = Expense.objects.filter(time__contains=keyword).order_by('-time')
        else:
            expense = Expense.objects.all().order_by('-time')
    else:
        return render(request, 'home.html')
    paginator = Paginator(expense, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'expense_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def addExpense(request):
    if request.user.role == 'Nhân viên bán hàng':
        if request.method == "POST":
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense = Expense(employee=request.user, time=datetime.now(),
                                  money=expense_form.cleaned_data['money'], type=expense_form.cleaned_data['type'],
                                  note=expense_form.cleaned_data['note'])
                expense.save()
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            expense_form = ExpenseForm()
    else:
        return render(request, 'home.html')
    return render(request, 'add_expense.html', {'expense_form': expense_form})


def preProcessing(df):
    df[3] = df[3] / 365
    df[0] = df[0] / 2494
    df[4] = df[4] / 2340
    df[6] = df[6] / 500000000
    df[5] = df[5] / 352
    return df


@login_required(login_url='/login/')
def salePredict(request):
    if request.user.role == 'admin':
        # khởi tạo model
        label_model = joblib.load('label.joblib')
        sale_model = joblib.load('sale.joblib')

        cursor = connection.cursor()

        # do tập dữ liệu lớn hơn ngày hiện tại -> set cứng date thay cho datetime.now()
        query = "select a.dt, a.motor_id, datediff('2024-1-2', a.dt) as import_date, " \
                "a.quantity, a.last_sale, a.export_price, a.name, a.image " \
                "from myapp_import_invoice " \
                "join (select myapp_motor.motor_id, myapp_motor.name, max(myapp_import_invoice.time) as dt, " \
                "myapp_motor.quantity, datediff('2024-1-2', max(myapp_delivery_invoice.time)) as last_sale, " \
                "myapp_motor.export_price, myapp_motor.image " \
                "from myapp_import_invoice " \
                "join myapp_import_motor on myapp_import_invoice.invoice_id = myapp_import_motor.invoice_id " \
                "join myapp_motor on myapp_import_motor.motor_id = myapp_motor.motor_id " \
                "join myapp_delivery_motor on myapp_motor.motor_id = myapp_delivery_motor.motor_id " \
                "join myapp_delivery_invoice on myapp_delivery_motor.invoice_id = myapp_delivery_invoice.invoice_id " \
                "group by myapp_motor.motor_id) as a on myapp_import_invoice.time = a.dt " \
                "order by a.motor_id"

        cursor.execute(query)

        df = []
        result = cursor.fetchall()
        for record in result:
            # bảng motor thêm cột sale_quantity sẽ bỏ qua được bước này :<
            query = "select ifnull((select sum(myapp_delivery_motor.quantity) " \
                    "from myapp_delivery_motor " \
                    "join myapp_delivery_invoice on myapp_delivery_motor.invoice_id = myapp_delivery_invoice.invoice_id " \
                    "where myapp_delivery_motor.motor_id = {s1} and myapp_delivery_invoice.time > '{s2}' " \
                    "group by myapp_delivery_motor.motor_id), 0) as sale_quantity".format(s1=record[1], s2=record[0])

            cursor.execute(query)
            # pass

            df.append([int(cursor.fetchall()[0][0])] + list(record))

        # df[0]: prev_quantity, df[1]: invoice_id, df[2]: motor_id, df[3]: import_date
        # df[4]: curr_quantity, df[5]: last_sale, df[6]: export_price df[7]: name, df[8]: image
        df = pd.DataFrame(df)
        # Dự đoán loại xe
        X_test = df.drop([1, 2, 7, 8], axis=1)
        X_test = preProcessing(X_test)
        proba_predictions = []
        for i in range(len(X_test)):
            proba_predictions.append(max(label_model.predict_proba(X_test)[i]))
        label_model.predict(X_test)
        predictions = label_model.predict(X_test)
        df['proba'] = proba_predictions
        # df1 chứa thông tin xe nên nhập, df chưa thông tin xe tồn kho
        df1 = df.copy()
        for i in range(len(predictions)):
            if predictions[i] == 0:
                df.drop(i, inplace=True)
                df1.drop(i, inplace=True)
            elif predictions[i] == 1:
                df.drop(i, inplace=True)
            else:
                df1.drop(i, inplace=True)
        # dự đoán % giảm
        x_test = df.drop([1, 2, 7, 8, 'proba'], axis=1)
        predictions = list(sale_model.predict(preProcessing(x_test)))
        for i in range(len(predictions)):
            predictions[i] = round(predictions[i], 1)

        df1['sale'] = [0] * len(df1)
        df['sale'] = predictions
        df1 = df1.drop([0, 1, 3, 4, 5, 6], axis=1)
        df = df.drop(([0, 1, 3, 4, 5, 6]), axis=1)
        results = pd.concat([df1, df], axis=0)
        results = results.values.tolist()

        for result in results:
            print(result)

        paginator = Paginator(results, 10)  # Show 25 contacts per page.

        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
    else:
        return render(request, 'home.html')
    return render(request, 'sale_predict.html', {'page_obj': page_obj})
