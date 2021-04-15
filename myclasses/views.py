from django.shortcuts import render, get_object_or_404
from .models import AllClasses
from myaccount.models import UserAccount
from .forms import AllClassesForm
from django.contrib import messages

# Create your views here.


def myclasses(request):
    """ Creates new classes if the user is authenticated as 'teacher' """
    if request.user.is_authenticated:
        teacher = get_object_or_404(UserAccount, user=request.user)
        if request.method == 'POST':
            form = AllClassesForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.added_by = teacher
                new_class.save()
                messages.success(request, 'Class added successfully')
        else:
            form = AllClassesForm()

        template = 'myclasses/myclasses.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
    else:
        template = 'myclasses/myclasses.html'
        return render(request, template)
