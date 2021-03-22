from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to show the home page """

    return render(request, 'home/index.html')
