from django.urls import path
from . import views

urlpatterns = [

    path('', views.report_dashboard, name='report_dashboard'),
  
   
  
    path(
        'load-subcategories/',
        views.load_subcategories,
        name='load_subcategories'
    ),
    path('date_wise_ledger/', views.date_wise_ledger, name='date_wise_ledger'),
    path('stock_summary/', views.stock_summary_form, name='stock_summary_form'),
    path('stock-summary/result/', views.stock_summary_report, name='stock_summary_report'),
   

]
