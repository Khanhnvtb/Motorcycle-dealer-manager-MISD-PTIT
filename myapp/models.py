from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils import timezone


class User(models.Model):
    user_id = models.AutoField(primary_key=True, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.CharField(max_length=100, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=20, blank=False, null=False)


class Employee(models.Model):
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, blank=False, null=False)
    salary = models.IntegerField(blank=False, null=False)


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)


class Import_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, blank=False, null=False)
    time = models.DateTimeField(default=timezone.datetime.now())
    total = models.IntegerField(blank=False, null=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, null=False)


class Motor(models.Model):
    motor_id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    brand = models.CharField(max_length=100, blank=False, null=False)
    image = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    assurance = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    import_price = models.IntegerField(blank=False, null=False)
    export_price = models.IntegerField(blank=False, null=False)


class Import_Motor(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    invoice_id = models.ForeignKey(Import_Invoice, on_delete=models.CASCADE, blank=False, null=False)
    motor_id = models.ForeignKey(Motor, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    owner = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)


class Delivery_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, blank=False, null=False)
    time = models.DateTimeField(default=timezone.datetime.now())
    total = models.IntegerField(blank=False, null=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)


class Delivery_Motor(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    invoice_id = models.ForeignKey(Delivery_Invoice, on_delete=models.CASCADE, blank=False, null=False)
    motor_id = models.ForeignKey(Motor, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
