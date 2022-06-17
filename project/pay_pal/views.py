from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Product, Order

# Create your views here.


def simpleCheckout(request):
	return render(request, 'pay_pal/simple-checkout.html')


def demo_store(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'pay_pal/demo_store.html', context)


def checkout(request, pk):
	product = Product.objects.get(id=pk)
	context = {'products': product}
	return render(request, 'pay_pal/product_checkout.html')

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	return JsonResponse('Payment completed!', safe=False)