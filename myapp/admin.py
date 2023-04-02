from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Motor)
admin.site.register(Store)
admin.site.register(Supplier)
admin.site.register(Employee)

