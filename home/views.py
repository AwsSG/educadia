from django.shortcuts import render
from myclasses.models import AllClasses
from myaccount.models import UserAccount

# Create your views here.


def index(request):
    """ A view to show the home page """
    teachers = UserAccount.objects.filter(user_type='teacher')
    classes = AllClasses.objects.all()
    context = {
        'teachers': teachers,
        'classes': classes,
    }

    return render(request, 'home/index.html', context)
