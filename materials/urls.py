from django.urls import path
from . import views

urlpatterns = [

    path('master/', views.material_master, name='material_master'),
    path('receipt/', views.material_receipt, name='material_receipt'),
    path('requisition/', views.material_requisition, name='material_requisition'),
    path('outward/', views.material_outward, name='material_outward'),

]