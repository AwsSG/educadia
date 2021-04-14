from django.shortcuts import render, get_object_or_404
from .models import AllClasses
from .forms import AllClassesForm
from django.contrib import messages

# Create your views here.


def myclasses(request):
    """ Creates new classes if the user is authenticated as 'teacher' """
    if request.user.is_authenticated:
        form = AllClassesForm()
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Class added successfully')
        template = 'myclasses/myclasses.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
    else:
        template = 'myclasses/myclasses.html'
        return render(request, template)
