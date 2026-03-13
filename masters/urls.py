from django.urls import path
from . import views

urlpatterns = [

    path('category/', views.category, name='category'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),

    path('subcategory/', views.subcategory, name='subcategory'),
    path('subcategory/edit/<int:id>/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategory/delete/<int:id>/', views.subcategory_delete, name='subcategory_delete'),

    # Unit Master
    path('unit/', views.unit_master, name='unit_master'),
    path('unit/edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('unit/delete/<int:id>/', views.unit_delete, name='unit_delete'),

    # Type Of Seller
    path('seller-type/', views.seller_type, name='seller_type'),
    path('seller-type/edit/<int:id>/', views.seller_type_edit, name='seller_type_edit'),
    path('seller-type/delete/<int:id>/', views.seller_type_delete, name='seller_type_delete'),

    # Work Spots
    path('work-spots/', views.work_spots, name='work_spots'),
    path('work-spots/edit/<int:id>/', views.work_spots_edit, name='work_spots_edit'),
    path('work-spots/delete/<int:id>/', views.work_spots_delete, name='work_spots_delete'),

    # Party Master
    path('party-master/', views.party_master, name='party_master'),
    path('party-master/edit/<int:id>/', views.party_master_edit, name='party_master_edit'),
    path('party-master/delete/<int:id>/', views.party_master_delete, name='party_master_delete'),


    path('load-subcategory/<int:id>/', views.load_subcategory, name='sub_category'),

]