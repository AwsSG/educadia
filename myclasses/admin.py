from django.contrib import admin
from .models import AllClasses, AllMaterials
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


class AllMaterialsAdmin(admin.ModelAdmin):
    list_display = (
        'added_by',
        'for_class',
        'name',
        'doc',
        'link',
    )


admin.site.register(AllClasses, MyClassesAdmin)
admin.site.register(AllMaterials, AllMaterialsAdmin)
