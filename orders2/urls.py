from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_info, name='customer_info'),
    path('menu/', views.menu, name='menu'),
]