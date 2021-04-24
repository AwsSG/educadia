from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import AllClasses, AllMaterials, ClassRegister
from myaccount.models import UserAccount
from .forms import AllClassesForm, AllMaterialsForm, ClassRegisterForm
from django.contrib import messages

# Create your views here.


def myclasses(request):
    """ view to add or join classes based on user type """
    if request.user.is_authenticated:
        teacher = get_object_or_404(UserAccount, user=request.user)
        student = None
        form = AllClassesForm()
        join_form = ClassRegisterForm()
        if teacher.user_type != 'student':
            # Creates new classes if the user is authenticated as 'teacher'
            if request.method == 'POST':
                form = AllClassesForm(request.POST)
                if form.is_valid():
                    new_class = form.save(commit=False)
                    new_class.added_by = teacher
                    new_class.save()
                    messages.success(request, 'Class added successfully')
            else:
                form = AllClassesForm()
        else:
            # joins classes if user is authenticated as 'student'
            student = get_object_or_404(UserAccount, user=request.user)
            if request.method == 'POST':
                join_form = ClassRegisterForm(request.POST)
                class_code = AllClasses.objects.filter(id=join_form['registered_for'].value())[0].class_join_code
                given_code = join_form['join_code'].value()
                already_registered = ClassRegister.objects.filter(join_code=given_code, student_name=student)
                if not already_registered:  # check if student already registered for that class
                    if class_code == given_code:
                        if join_form.is_valid:
                            new_student = join_form.save(commit=False)
                            new_student.student_name = student
                            new_student.save()
                            messages.success(request, 'You joined class successfully')
                            join_form = ClassRegisterForm()
                    else:
                        messages.success(request, 'The join code you entered for the selected class is incorrect')
                else:
                    messages.success(request, 'You are already registered for this class')

        template = 'myclasses/myclasses.html'
        all_classes = AllClasses.objects.filter(added_by=teacher)
        registered_classes = ClassRegister.objects.filter(student_name=student).values_list('registered_for', flat=True)
        joined_classes = AllClasses.objects.filter(id__in=registered_classes)
        context = {
            'form': form,
            'all_classes': all_classes,
            'join_form': join_form,
            'joined_classes': joined_classes,
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
    # check if user is a teacher
    if teacher.user_type != 'student':
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

    class_materials = AllMaterials.objects.filter(for_class=a_class)
    context = {
        'form_upload': form_upload,
        'form': form,
        'class': a_class,
        'class_materials': class_materials
    }

    return render(request, 'myclasses/edit_class.html', context)


def delete_class(request, class_id):
    """delete selected class"""
    class_to_delete = get_object_or_404(AllClasses, pk=class_id)
    class_to_delete.delete()
    messages.success(request, 'Class deleted successfully')
    return redirect(reverse('myclasses'))


def material_detail(request, material_id):
    """A view to edit a material"""
    material = get_object_or_404(AllMaterials, pk=material_id)
    if request.method == 'POST':
        form_upload = AllMaterialsForm(request.POST, request.FILES, instance=material)
        if form_upload.is_valid:
            form_upload.save()
            messages.success(request, 'Changes saved successfully')

    form_upload = AllMaterialsForm(instance=material)
    context = {
        'material': material,
        'form_upload': form_upload
    }
    return render(request, 'myclasses/edit_material.html', context)


def delete_material(request, material_id):
    """delete selected material"""
    material_to_delete = get_object_or_404(AllMaterials, pk=material_id)
    class_id = material_to_delete.for_class.id
    material_to_delete.delete()
    messages.success(request, 'Material deleted successfully')
    return redirect(reverse('class_detail', args=[class_id]))
