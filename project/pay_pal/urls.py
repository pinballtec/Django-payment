from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.simpleCheckout, name='simple_checkout'),
]