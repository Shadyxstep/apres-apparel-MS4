from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is currently empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IjipxA3wCHF4RV10FYBhtTKTLBuR7Zo0osXnAmyKjpUSfBiLNJ32dtXQ841BXiIhNTV5huPytswhFpmaK27L6nk00yJjCV8Kz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)