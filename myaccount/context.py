from django.shortcuts import get_object_or_404
from .models import UserAccount


def current_user(request):
    if request.user.is_authenticated:
        account = get_object_or_404(UserAccount, user=request.user)
        fname = account.first_names
        lname = account.last_name
        user_type = account.user_type

        context = {
            'fname': fname,
            'lname': lname,
            'user_type': user_type,
        }
    else:
        context = {}

    return context
