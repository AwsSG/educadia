from django.urls import path
from . import views

urlpatterns = [
    path('', views.myclasses, name='myclasses'),
    path('edit/<int:class_id>/', views.class_detail, name='class_detail'),
    path('delete/<int:class_id>/', views.delete_class, name='delete_class'),
]
