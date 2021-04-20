from django.urls import path
from . import views

urlpatterns = [
    path('', views.myclasses, name='myclasses'),
    path('<int:class_id>', views.class_detail, name='class_detail'),
]
