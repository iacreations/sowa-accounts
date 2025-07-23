from django.urls import path
from . import views


app_name='sowaf'
# my urls
urlpatterns = [
    path('home/', views.home, name='home'),
    # asset urls
    path('assets/', views.assets, name='assets'),
    path('assets/add/asset', views.add_assests, name='add-asset'),
    path('assets/edit/<str:pk>/', views.edit_asset, name='edit-asset'),
    # customer urls
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add_customer, name='add-customer'),
    path('customers/edit/<str:pk>/', views.edit_customer, name='edit-customer'),
    path('customer/delete/<str:pk>/', views.delete_customer, name='delete-customer'),
    # clents urls
    path('clients/', views.clients, name='clients'),
    path('clients/add/', views.add_client, name='add-client'),
    path('clients/edit/<str:pk>/', views.edit_client, name='edit-client'),
    path('clients/delete/<str:pk>/', views.delete_client, name='delete-client'),
    # employee urls
    path('employees/', views.employee, name='employees'),
    path('employees/add/employee', views.add_employees, name='add-employee'),
    path('employees/edit/<str:pk>/', views.edit_employee, name='edit-employee'),
    path('employees/delete/<str:pk>/', views.delete_employee, name='delete-employee'),
    # --------------
    path('miscellaneous/', views.miscellaneous, name='miscellaneous'),
    # -------------
    path('reports/', views.reports, name='reports'),
    # -----------------
    path('sales/', views.sales, name='sales'),
    path('sales/add/invoice', views.add_invoice, name='add-invoice'),
    path('sales/add/receipts', views.add_receipt, name='add-receipt'),
    path('sales/add/payments', views.add_payment, name='add-payments'),
    path('sales/add/products', views.add_products, name='add-products'),
    path('sales/add/invoice', views.add_invoice, name='add-invoice'),
    # supplier urls
    path('suppliers/', views.supplier, name='suppliers'),
    path('supplier/add/suppliers', views.add_suppliers, name='add-suppliers'),
    path('supplier/edit/<str:pk>', views.edit_supplier, name='edit-supplier'),
    path('supplier/delete/<str:pk>', views.delete_supplier, name='delete-supplier'),
    path('expenses/', views.expenses, name='expenses'),
    path('tasks/', views.tasks, name='tasks'),
    path('taxes/', views.taxes, name='taxes'),
    # path('invoices/', views.invoice, name='invoices'),
    path('invoices/add/invoice', views.add_invoice, name='add-invoice'),
    # path('receipts/', views.receipt, name='receipts'),
    path('receipts/add/receipt', views.add_receipt, name='add-receipt'),
    # path('payments/', views.payment, name='payments'),
    path('payments/add/payment', views.add_payment, name='add-payment'),
    
]
