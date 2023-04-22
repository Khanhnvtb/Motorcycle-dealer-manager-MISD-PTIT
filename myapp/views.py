from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.forms import formset_factory
import os
from .forms import *
from .models import *
from datetime import date, timedelta
from django.db import connection


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


@login_required(login_url='/login/')
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
    if request.user.role == 'admin':
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
    paginator = Paginator(stores, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'store_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def addSupplier(request):
    if request.user.role != 'Nhân viên bán hàng':
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
    if request.user.role == "admin":
        if request.method == "POST":
            keyword = request.POST.get('keyword', None)
            users = User.objects.filter(name__contains=keyword)
        else:
            users = User.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(users, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'user_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def storeManager(request):
    if request.user.role != "Nhân viên kho":
        if request.method == "POST":
            keyword = request.POST.get('keyword', None)
            stores = Store.objects.filter(name__contains=keyword)
        else:
            stores = Store.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(stores, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'store_manager.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def motorManager(request):
    if request.user.role != 'Nhân viên bán hàng':
        if request.method == "POST":
            keyword = request.POST.get('keyword', None)
            motors = Motor.objects.filter(name__contains=keyword)
        else:
            motors = Motor.objects.all()
    else:
        return render(request, 'home.html')
    paginator = Paginator(motors, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'motor_manager.html', {"page_obj": page_obj})


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
                messages.add_message(request, messages.SUCCESS, 'Bạn chưa chọn các sản phẩm cần nhập')
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
                messages.add_message(request, messages.SUCCESS, 'Bạn chưa chọn các sản phẩm cần xuất')
            else:
                for motor in export_dict.keys():
                    quantity = export_dict[motor]
                    if motor.quantity < quantity:
                        storage = messages.get_messages(request)
                        storage.used = True
                        messages.add_message(request, messages.SUCCESS,
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
def reportView(request):
    return render(request, 'report.html')


def getStartDate(year, month):
    # tạo một đối tượng date với năm và tháng đã nhập
    d = date(year, month, 1)

    # lấy ra ngày bắt đầu của tháng
    start_date = d.replace(day=1)
    return start_date


def getEndDate(year, month):
    # tạo một đối tượng date với năm và tháng đã nhập
    d = date(year, month, 1)

    # lấy ra ngày bắt đầu và ngày kết thúc của tháng
    end_date = d.replace(month=month + 1, day=1) - timedelta(days=1)
    return end_date


@login_required(login_url='/login/')
def reportTurnover(request):
    if request.user.role == 'admin':
        results = ()
        if request.method == "POST":
            date_form = DateForm(request.POST)
            if date_form.is_valid():
                start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                          int(date_form.cleaned_data['start_month']))
                end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
                if start_date > end_date:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_delivery_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by month(time) order by Month_sale".format(s1="%Y-%m",
                                                                              s2=str(start_date),
                                                                              s3=str(end_date))

                    # chạy câu lệnh SQL bằng phương thức execute()
                    cursor.execute(query)

                    # lấy ra kết quả bằng phương thức fetchall()
                    results = cursor.fetchall()

                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, 'Thành công')
        else:
            date_form = DateForm()
    else:
        return render(request, 'home.html')
    paginator = Paginator(results, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'report_turnover.html', {'date_form': date_form, 'page_obj': page_obj})


@login_required(login_url='/login/')
def reportSaleItems(request):
    report = {}
    if request.method == "POST":
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            start_date = getStartDate(int(date_form.cleaned_data['start_year']),
                                      int(date_form.cleaned_data['start_month']))
            end_date = getEndDate(int(date_form.cleaned_data['end_year']), int(date_form.cleaned_data['end_month']))
            if start_date > end_date:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
            else:
                # tạo một con trỏ cho cơ sở dữ liệu
                cursor = connection.cursor()

                query = "SELECT date_format(Time, '{s1}') as Month_sale, " \
                        "myapp_Motor.image, myapp_Motor.name, SUM(myapp_Delivery_Motor.quantity) AS quantity " \
                        "FROM myapp_Motor " \
                        "JOIN myapp_Delivery_Motor ON myapp_Motor.motor_Id = myapp_Delivery_Motor.motor_Id " \
                        "JOIN myapp_delivery_invoice ON myapp_delivery_motor.invoice_id = myapp_delivery_invoice.invoice_id " \
                        "WHERE myapp_delivery_invoice.time between '{s2}' AND '{s3}' " \
                        "GROUP BY Month(time), myapp_Motor.name, myapp_Motor.Image " \
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
    paginator = Paginator(list(report), 2)  # Show 2 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'report_sale_items.html', {'date_form': date_form, 'page_obj': page_obj})


@login_required(login_url='/login/')
def reportBestSaleItems(request):
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
    return render(request, 'report_best_sale_items.html', {'page_obj': page_obj})


@login_required(login_url='/login/')
def saleHistory(request, username):
    if request.user.role == 'admin':
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


@login_required(login_url='/login/')
def importHistory(request, username):
    if request.user.role != 'Nhân viên bán hàng':
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
def visualization(request):
    return render(request, 'visualization.html')


@login_required(login_url='/login/')
def visualizationTurnover(request):
    if request.user.role == 'admin':
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
                    messages.add_message(request, messages.SUCCESS, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
                else:
                    # tạo một con trỏ cho cơ sở dữ liệu
                    cursor = connection.cursor()

                    query = "select date_format(time, '{s1}') as Month_sale, SUM(total) as sales " \
                            "from myapp_delivery_invoice " \
                            "where time between '{s2}' and '{s3}'" \
                            "group by month(time) order by Month_sale".format(s1="%Y-%m",
                                                                              s2=str(start_date),
                                                                              s3=str(end_date))

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
    return render(request, 'visualization_turnover.html',
                  {'date_form': date_form, 'columns_name': columns_name, 'values': values})


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
                messages.add_message(request, messages.SUCCESS, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
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


@login_required(login_url='/login/')
def visualizationKpiUser(request, username):
    if request.user.role == 'admin':
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
                    messages.add_message(request, messages.SUCCESS, 'Thời điểm bắt đầu không được lớn hơn kết thúc')
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


@login_required(login_url='/login/')
def importReceipt(request):
    if request.user.role == "Nhân viên kho":
        if request.method == "POST":
            import_form = ImportReceiptForm(request.POST)
            if import_form.is_valid():
                employee_id = request.user.id
                import_invoice = import_form.cleaned_data.get('import_invoice')
                time = date.today()
                money = import_form.cleaned_data.get('money')
                note = import_form.cleaned_data.get('note')
                max_money = import_invoice.total - import_invoice.payment
                if money > max_money:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, f'Số tiền không được lớn hơn {max_money}')
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
    return render(request, 'import_receipt.html', {'import_receipt_form': import_form})


@login_required(login_url='/login/')
def exportReceipt(request):
    if request.user.role == "Nhân viên bán hàng":
        if request.method == "POST":
            export_form = ExportReceiptForm(request.POST)
            if export_form.is_valid():
                employee_id = request.user.id
                export_invoice = export_form.cleaned_data.get('delivery_invoice')
                time = date.today()
                money = export_form.cleaned_data.get('money')
                note = export_form.cleaned_data.get('note')
                max_money = export_invoice.total - export_invoice.payment
                if money > max_money:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.add_message(request, messages.SUCCESS, f'Số tiền không được lớn hơn {max_money}')
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
    return render(request, 'export_receipt.html', {'export_receipt_form': export_form})
