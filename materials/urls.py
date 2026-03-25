from django.urls import path
from . import views

urlpatterns = [

    path('master/', views.material_master, name='material_master'),
    path('master/<int:pk>/', views.material_master, name='material_master'),  # for edit
    path('material-delete/<int:pk>/', views.material_delete, name='material_delete'),
    path('load-subcategory/', views.load_subcategory, name='load_subcategory'),
    path('receipt/', views.material_receipt, name='material_receipt'),
    path('receipt/<int:pk>/', views.material_receipt, name='material_receipt'), # Edit
    path('receipt/delete/<int:pk>/', views.material_receipt_delete, name='material_receipt_delete'),
    path('requisition/', views.material_requisition, name='material_requisition'),           # Create + List
    path('requisition/<int:pk>/', views.material_requisition, name='material_requisition'), # Edit
    path('requisition/delete/<int:pk>/', views.material_requisition_delete, name='material_requisition_delete'),
    path('outward/', views.material_outward, name='material_outward'),                    # Create + List + Edit
    path('outward/<int:pk>/', views.material_outward, name='material_outward'),          # Edit
    path('outward/delete/<int:pk>/', views.material_outward_delete, name='material_outward_delete'),
    path('outward/fetch-receipt/', views.fetch_receipt_by_entry, name='fetch_receipt_by_entry'),

]