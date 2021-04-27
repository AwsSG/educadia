from django.shortcuts import render
from .forms import DonateForm


def donate(request):
    donate_form = DonateForm()
    context = {
        'donate_form': donate_form
    }

    return render(request, 'donate/donate.html', context)
