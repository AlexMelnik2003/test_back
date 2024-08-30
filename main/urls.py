from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('menu/', views.menu, name='menu'),
]