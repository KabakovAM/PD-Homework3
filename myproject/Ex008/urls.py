from django.urls import path
from . import views

urlpatterns = [
    path('client_orders_by_time/<int:client_id>/', views.client_orders_by_time, name='client_orders_by_time'),
]