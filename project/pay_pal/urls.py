from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.simpleCheckout, name='simple_checkout'),
    path('store/', views.demo_store, name='store'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('complete/', views.paymentComplete, name='complete'),
]