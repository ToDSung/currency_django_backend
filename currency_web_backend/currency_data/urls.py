from django.urls import path
from . import views

urlpatterns = [
    path('', views.here, name='world')
]