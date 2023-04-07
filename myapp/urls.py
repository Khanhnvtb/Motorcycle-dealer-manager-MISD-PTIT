from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('show_user/', views.showUser, name='show_user'),
    path('user_manager/', views.userManager, name='user_manager'),
    path('add_user/', views.addUser, name='add_user'),

    path('show_motor/', views.showMotor, name='show_motor'),
    path('motor_manager/', views.motorManager, name='motor_manager'),
    path('add_motor/', views.addMotor, name='add_motor'),

    path('show_store', views.showStore, name='show_store'),
    path('store_manager/', views.storeManager, name='store_manager'),
    path('add_store/', views.addStore, name='add_store'),

    path('show_supplier/', views.addSupplier, name='show_supplier'),
    path('supplier_manager/', views.supplierManager, name='supplier_manager'),
    path('add_supplier/', views.addSupplier, name='add_supplier'),

]
