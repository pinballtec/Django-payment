from django.urls import path
from . import views

urlpatterns = [
    path('success/<str:args>/', views.success, name='success'),
    path('', views.test, name='index'),
    path('charge/', views.charge, name='charge'),
]