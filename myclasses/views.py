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
        all_classes = AllClasses.objects.filter(added_by=teacher)
        context = {
            'form': form,
            'all_classes': all_classes,
        }
        return render(request, template, context)
    else:
        template = 'myclasses/myclasses.html'
        return render(request, template)


def class_detail(request, class_id):
    """ A view for individual class details """
    a_class = get_object_or_404(AllClasses, pk=class_id)

    if request.method == 'POST':
        form = AllClassesForm(request.POST, instance=a_class)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class details updated successfully')

        form = AllClassesForm(instance=a_class)
    else:
        form = AllClassesForm(instance=a_class)
    context = {
        'form': form,
        'class': a_class
    }

    return render(request, 'myclasses/a_class.html', context)
