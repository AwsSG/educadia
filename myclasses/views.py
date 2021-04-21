from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import AllClasses, AllMaterials
from myaccount.models import UserAccount
from .forms import AllClassesForm, AllMaterialsForm
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
    form_upload = AllMaterialsForm()
    form = AllClassesForm(instance=a_class)
    teacher = get_object_or_404(UserAccount, user=request.user)
    # edit class POST handler
    if request.method == 'POST' and 'edit_class_form' in request.POST:
        form = AllClassesForm(request.POST, instance=a_class)
        if form.is_valid():
            form.save()
            messages.success(request, 'Class details updated successfully')

        form = AllClassesForm(instance=a_class)
    # add material POST handler
    elif request.method == 'POST' and 'add_material_form' in request.POST:
        form_upload = AllMaterialsForm(request.POST, request.FILES)
        if form_upload.is_valid():
            new_material = form_upload.save(commit=False)
            new_material.added_by = teacher
            new_material.for_class = a_class
            new_material.save()
            messages.success(request, 'Material uploaded successfully')

        form_upload = AllMaterialsForm()
    else:
        form = AllClassesForm(instance=a_class)

    class_materials = AllMaterials.objects.filter(added_by=teacher, for_class=a_class)
    context = {
        'form_upload': form_upload,
        'form': form,
        'class': a_class,
        'class_materials': class_materials
    }

    return render(request, 'myclasses/a_class.html', context)
