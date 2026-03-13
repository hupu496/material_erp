from django.urls import path
from . import views

urlpatterns = [

    path('', views.report_dashboard, name='report_dashboard'),
    path('master/', views.master_report, name='master_report'),
    path('stock/', views.stock_summary, name='stock_summary'),
    path('returnable/', views.returnable_report, name='returnable_report'),

]