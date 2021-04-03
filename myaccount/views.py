from django.shortcuts import render, get_object_or_404
from .models import UserAccount
# Create your views here.


def myaccount(request):
    """ Display the user's account """
    account = get_object_or_404(UserAccount, user=request.user)

    template = 'myaccount/myaccount.html'
    context = {
        'account': account,
    }

    return render(request, template, context)
