from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import DonateForm
from django.conf import settings
import stripe


def donate(request):
    """
    Donation view to handle payments
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_total = 1 * 100

    if request.method == 'POST':
        donate_form = DonateForm(request.POST)
        if donate_form.is_valid():
            donated_amount = donate_form['amount'].value()
            stripe_total = round(float(donated_amount) * 100)
            donate_form.save()
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            messages.success(request, 'Thank you for your donation!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Form incorrect, make sure you fill the \
                required fields correctly')
    else:
        donate_form = DonateForm()
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

    context = {
        'donate_form': donate_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'donate/donate.html', context)
