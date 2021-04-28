from django.shortcuts import render
from .forms import DonateForm


def donate(request):
    donate_form = DonateForm()
    context = {
        'donate_form': donate_form,
        'stripe_public_key':
        'pk_test_51IkYXvIT9OmxcWEwyhVrcIDxF3KoC2xFLKc7nclICOdiZgRIpjAMhiMvAnfAiRlwNZDnPlegDXWoQGTkxJnYQ0ae00ofJ7siq9',
        'client_secret': 'test client secret'
    }

    return render(request, 'donate/donate.html', context)
