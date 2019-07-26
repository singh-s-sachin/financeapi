from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('debit', views.debit),
    path('credit', views.credit),
    path('show',views.showtransactions),
]