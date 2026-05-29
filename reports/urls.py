from django.urls import path
from . import views

urlpatterns = [

    path('', views.report_dashboard, name='report_dashboard'),
  
    path('stock/', views.stock_summary, name='stock_summary'),
  
    path(
        'load-subcategories/',
        views.load_subcategories,
        name='load_subcategories'
    ),
    path('date_wise_ledger/', views.date_wise_ledger, name='date_wise_ledger'),
    path('stock_summary/', views.stock_summary, name='stock_summary'),
     

]
