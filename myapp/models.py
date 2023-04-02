from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=20)


class Employee(models.Model):
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    salary = models.IntegerField()


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)


class Import_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    time = models.DateField()
    total = models.IntegerField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Motor(models.Model):
    motor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    assurance = models.CharField(max_length=100)
    quantity = models.IntegerField()
    import_price = models.IntegerField()
    export_price = models.IntegerField()


class Import_Motor(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Import_Invoice, on_delete=models.CASCADE)
    motor_id = models.ForeignKey(Motor, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)


class Delivery_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    time = models.DateField()
    total = models.IntegerField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)


class Delivery_Motor(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Delivery_Invoice, on_delete=models.CASCADE)
    motor_id = models.ForeignKey(Motor, on_delete=models.CASCADE)
    quantity = models.IntegerField()
