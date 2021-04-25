from django.shortcuts import render, get_object_or_404
from .models import UserAccount
from .forms import UserAccountForm
from django.contrib import messages
# Create your views here.


def myaccount(request):
    """ Display the user's account """
    if request.user.is_authenticated:
        account = get_object_or_404(UserAccount, user=request.user)
        if request.method == 'POST':
            form = UserAccountForm(request.POST, request.FILES, instance=account)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(request, 'Form incorrect, make sure you fill the required fields correctly')

        form = UserAccountForm(instance=account)

        template = 'myaccount/myaccount.html'
        context = {
            'account': account,
            'form': form,
        }
        return render(request, template, context)
    else:
        template = 'myaccount/myaccount.html'
        return render(request, template)
