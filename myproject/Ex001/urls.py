from django.urls import path
from . import views

urlpatterns = [
    path('about_django/', views.about_django, name='dabout_django'),
    path('about_me/', views.about_me, name='about_me')
]