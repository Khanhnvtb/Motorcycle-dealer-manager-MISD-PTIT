# Generated by Django 4.1.7 on 2023-04-06 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_user_dob_alter_delivery_invoice_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='delivery_invoice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 19, 42, 0, 956982)),
        ),
        migrations.AlterField(
            model_name='import_invoice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 19, 42, 0, 955986)),
        ),
    ]