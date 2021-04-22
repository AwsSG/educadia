from django.urls import path
from . import views

urlpatterns = [
    path('', views.myclasses, name='myclasses'),
    path('edit_class/<int:class_id>/', views.class_detail, name='class_detail'),
    path('delete/<int:class_id>/', views.delete_class, name='delete_class'),
    path('edit_material/<int:material_id>/', views.material_detail, name='material_detail'),
]
