from django.shortcuts import render, get_object_or_404
from .models import UserAccount
from .forms import UserAccountForm
from django.contrib import messages
# Create your views here.


def myaccount(request):
    """ Display the user's account """
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserAccountForm(instance=account)

    template = 'myaccount/myaccount.html'
    context = {
        'account': account,
        'form': form,
    }

    return render(request, template, context)
