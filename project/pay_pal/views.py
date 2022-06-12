from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Product, Order

# Create your views here.


def simpleCheckout(request):
	return render(request, 'base/simple_checkout.html')
