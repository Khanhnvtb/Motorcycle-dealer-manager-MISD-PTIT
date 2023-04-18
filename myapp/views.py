from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    os.remove(f"myapp/static/media/{user.avatar}")
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
    os.remove(f"myapp/static/media/{motor.image}")
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
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        users = User.objects.filter(name__contains=keyword)
    else:
        users = User.objects.all()
    return render(request, 'user_manager.html', {'users': users})


@login_required(login_url='/login/')
def storeManager(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        stores = Store.objects.filter(name__contains=keyword)
    else:
        stores = Store.objects.all()
    return render(request, 'store_manager.html', {'stores': stores})


@login_required(login_url='/login/')
def motorManager(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        motors = Motor.objects.filter(name__contains=keyword)
    else:
        motors = Motor.objects.all()
    return render(request, 'motor_manager.html', {'motors': motors})


@login_required(login_url='/login/')
def supplierManager(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        suppliers = Supplier.objects.filter(name__contains=keyword)
    else:
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
def importMotor(request):
    context = {}

    # creating a formset and 5 instances of ImportForm
    ImportFormSet = formset_factory(ImportForm, extra=5)
    import_forms = ImportFormSet(request.POST or None)
    supplier_form = ImportFromSupplierFrom(request.POST or None)

    if supplier_form.is_valid() and import_forms.is_valid():
        supplier = supplier_form.cleaned_data['supplier']
        employee = request.user
        import_dict = {}
        for import_form in import_forms:
            motor = import_form.cleaned_data.get('motor')
            quantity = import_form.cleaned_data.get('quantity')
            if motor and quantity:
                if motor in import_dict.keys():
                    import_dict[motor] += quantity
                else:
                    import_dict[motor] = quantity
        for motor in import_dict.keys():
            quantity = import_dict[motor]
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
        if len(import_dict):
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Nhập hàng thàng công')
            import_forms = ImportFormSet()
            supplier_form = ImportFromSupplierFrom()
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Bạn chưa chọn các sản phẩm cần nhập')
    context['import_forms'] = import_forms
    context['supplier_form'] = supplier_form
    return render(request, "import_motor.html", context)


@login_required(login_url='/login/')
def exportMotor(request):
    context = {}

    # creating a formset and 5 instances of ExportForm
    ExportFormSet = formset_factory(ExportForm, extra=5)
    export_forms = ExportFormSet(request.POST or None)
    store_form = ExportToStoreForm(request.POST or None)

    if store_form.is_valid() and export_forms.is_valid():
        store = store_form.cleaned_data['store']
        employee = request.user
        export_dict = {}
        for export_form in export_forms:
            employee = request.user
            motor = export_form.cleaned_data.get('motor')
            quantity = export_form.cleaned_data.get('quantity')
            if motor and quantity:
                if motor in export_dict.keys():
                    export_dict[motor] += quantity
                else:
                    export_dict[motor] = quantity
        for motor in export_dict.keys():
            quantity = export_dict[motor]
            if motor.quantity < quantity:
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, f'Số lượng {motor} trong kho chỉ còn {motor.quantity}')
                context['export_forms'] = export_forms
                context['store_form'] = store_form
                return render(request, "export_motor.html", context)
        for motor in export_dict.keys():
            quantity = export_dict[motor]
            motor.quantity -= quantity
            motor.save()
            delivery_invoice = Delivery_Invoice(total=quantity * motor.export_price,
                                                employee_id=employee.id,
                                                store_id=store.store_id)
            delivery_invoice.save()
            delivery_motor = Delivery_Motor(invoice_id=delivery_invoice.invoice_id,
                                            motor_id=motor.motor_id,
                                            quantity=quantity)
            delivery_motor.save()
        if len(export_dict):
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Xuất hàng thàng công')
            export_forms = ExportFormSet()
            store_form = ExportToStoreForm()
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.add_message(request, messages.SUCCESS, 'Bạn chưa chọn các sản phẩm cần xuất')
    context['export_forms'] = export_forms
    context['store_form'] = store_form
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
    return render(request, 'report_turnover.html', {'date_form': date_form, 'report': results})


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
                for record in report:
                    print(record[0])
                    print(record[1])
                storage = messages.get_messages(request)
                storage.used = True
                messages.add_message(request, messages.SUCCESS, 'Thành công')
    else:
        date_form = DateForm()
    return render(request, 'report_sale_items.html', {'date_form': date_form, 'report': report})


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
    return render(request, 'report_best_sale_items.html', {'report': results})
