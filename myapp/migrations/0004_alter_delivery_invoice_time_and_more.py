# Generated by Django 4.2 on 2023-04-20 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_delivery_invoice_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_invoice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 14, 27, 30, 193169)),
        ),
        migrations.AlterField(
            model_name='import_invoice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 14, 27, 30, 191174)),
        ),
    ]