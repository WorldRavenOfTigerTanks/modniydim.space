from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'pages'

urlpatterns = [

    path('', index, name='index'),
    path('sales', sales, name='sales'),
    path('thanks', thanks, name='thanks'),
    path('cat/<str:slug>/', category_view, name='category_view'),
    path('view/<str:slug_prod>', single, name='single'),
    path('info/<str:page_slug>', pages, name='pages'),
    path('basket/add/<int:product_id>', add_to_basket, name='add_to_basket'),
    path('basket/remove/<int:basket_id>/<int:prod_id>/<str:size>/<str:color>', remove_basket, name='remove_basket')

]