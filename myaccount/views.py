from django.shortcuts import render

# Create your views here.


def myaccount(request):
    """ Display the user's account """

    template = 'myaccount/myaccount.html'
    context = {}

    return render(request, template, context)
