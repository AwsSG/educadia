from django.contrib import admin
from .models import AllClasses
# Register your models here.


class MyClassesAdmin(admin.ModelAdmin):
    list_display = (
        'class_name',
        'added_by',
        'class_join_code',
        'class_subject',
        'class_university',
        'class_collage',
        'class_department',
        'class_level',
        'class_division',
        'class_year'
    )


admin.site.register(AllClasses, MyClassesAdmin)
