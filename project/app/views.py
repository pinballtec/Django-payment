from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def test(request):
    return render(request, 'app/template.html')


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('ok', args=[amount]))


def success(request, args):
    amount = args
    return render(request, 'app/succes.html', {'amount': amount})