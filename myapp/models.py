from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField(upload_to='user_image/')
    dob = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=20, blank=False, null=False)
    salary = models.IntegerField(default=0, blank=False, null=False)


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Import_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, blank=False, null=False)
    time = models.DateTimeField(default=timezone.datetime.now())
    total = models.IntegerField(blank=False, null=False)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False, null=False)


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

    def __str__(self):
        return self.name


class Import_Motor(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    invoice = models.ForeignKey(Import_Invoice, on_delete=models.CASCADE, blank=False, null=False)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    owner = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Delivery_Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, blank=False, null=False)
    time = models.DateTimeField(default=timezone.datetime.now())
    total = models.IntegerField(blank=False, null=False)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)


class Delivery_Motor(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    invoice = models.ForeignKey(Delivery_Invoice, on_delete=models.CASCADE, blank=False, null=False)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
