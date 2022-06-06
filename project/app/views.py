from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
# Create your views here.

stripe.api_key = 'sk_test_51L6KXLEwvLDVkswxjRwVjIgiccUalqwoZs1a9wDrlQIFDiEayKV7f2pTYsjEg3oDDSqBO4xZ5xgrX7x2DvAH2QeZ00g641Habd'


def test(request):
    return render(request, 'app/index.html')


def charge(request):

    amount = int(request.POST['amount'])

    if request.method == 'POST':
        print('Data:', request.POST)
        # user creation for stripe -->

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=100*amount,
            currency='usd',
            description='Donation',
        )

    return redirect(reverse('success', args=[amount]))


def success(request, args):
    amount = args
    return render(request, 'app/succes.html', {'amount': amount})