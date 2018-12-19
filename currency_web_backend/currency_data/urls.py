from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_currency_list, name='list'),
    path('<str:item>', views.get_currency_data),
]
