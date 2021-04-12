from django.shortcuts import render

# Create your views here.


def myclasses(request):
    """ Template that returns all the classes created/joined) """
    return render(request, 'myclasses/myclasses.html')
