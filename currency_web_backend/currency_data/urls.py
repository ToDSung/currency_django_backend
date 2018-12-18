from django.urls import path
from . import views

urlpatterns = [
    path('', views.here, name='world'),
    path('jpy', views.get_jpy_data, name='jpy'),
]