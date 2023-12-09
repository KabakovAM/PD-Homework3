from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:num>/', views.coin, name='coin'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('num/<int:num>/', views.num, name='num'),
]