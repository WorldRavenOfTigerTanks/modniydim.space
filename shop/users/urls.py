from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [

    #path('', single, name='single'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('basket/', basket, name='basket'),
]