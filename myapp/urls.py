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

    path('import_motor/', views.importMotor, name='import_motor'),
    path('export_motor/', views.exportMotor, name='export_motor'),

    path('report/', views.reportView, name='report'),
    path('report_turnover/', views.reportTurnover, name='report_turnover'),
    path('report_sale_items/', views.reportSaleItems, name='report_sale_items'),
    path('report_best_sale_items/', views.reportBestSaleItems, name='report_best_sale_items'),
    path('sale_history/<str:username>/', views.saleHistory, name='sale_history'),
    path('import_history/<str:username>/', views.importHistory, name='import_history'),
    path('report_sale_history/', views.reportSaleHistory, name='report_sale_history'),
    path('report_import_history/', views.reportImportHistory, name='report_import_history'),

    # path('motors/', views.getMotorByAPI,),
    
    path('visualization/', views.visualization, name='visualization'),
    path('visualization_turnover/', views.visualizationTurnover, name='visualization_turnover'),
    path('visualization_sale_items/', views.visualizationSaleItems, name='visualization_sale_items'),
    path('visualization_best_sale_items/', views.visualizationBestSaleItems, name='visualization_best_sale_items'),
    path('visualization_kpi_user/<str:username>/', views.visualizationKpiUser, name='visualization_kpi_user'),
    path('visualization_kpi/', views.visualizationKpi, name='visualization_kpi'),
    path('visualization_import_from_supplier/', views.visualizationImportFromSupplier,
         name='visualization_import_from_supplier'),
    path('visualization_export_to_store/', views.visualizationExportToStore, name='visualization_export_to_store'),

    path('import_receipt/', views.importReceipt, name='import_receipt'),
    path('export_receipt/', views.exportReceipt, name='export_receipt'),
]
