from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.donate, name="donate"),
    path('wh/', webhook, name='webhook'),
]
