from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('show_user/', views.showUser, name='show_user'),
    path('show_user/<str:username>/', views.showUser, name='show_user_by_username'),
    path('user_manager/', views.userManager, name='user_manager'),
    path('add_user/', views.addUser, name='add_user'),
    path('update_user/<str:username>/', views.updateUser, name='update_user'),
    path('delete_user/<str:username>/', views.deleteUser, name='delete_user'),

    path('show_motor/<int:motor_id>/', views.showMotor, name='show_motor'),
    path('motor_manager/', views.motorManager, name='motor_manager'),
    path('add_motor/', views.addMotor, name='add_motor'),
    path('update_motor/<int:motor_id>/', views.updateMotor, name='update_motor'),
    path('delete_motor/<int:motor_id>/', views.deleteMotor, name='delete_motor'),

    path('show_store/<int:store_id>/', views.showStore, name='show_store'),
    path('store_manager/', views.storeManager, name='store_manager'),
    path('add_store/', views.addStore, name='add_store'),
    path('update_store/<int:store_id>/', views.updateStore, name='update_store'),
    path('delete_store/<int:store_id>/', views.deleteStore, name='delete_store'),

    path('show_supplier/<int:supplier_id>/', views.showSupplier, name='show_supplier'),
    path('supplier_manager/', views.supplierManager, name='supplier_manager'),
    path('add_supplier/', views.addSupplier, name='add_supplier'),
    path('update_supplier/<int:supplier_id>/', views.updateSupplier, name='update_supplier'),
    path('delete_supplier/<int:supplier_id>/', views.deleteSupplier, name='delete_supplier'),

    path('import_motor/', views.formset_view, name='import_motor'),
]
