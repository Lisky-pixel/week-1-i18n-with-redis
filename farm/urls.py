from django.urls import path
from . import views

app_name = 'farm'

urlpatterns = [
    path('', views.produce_list, name='produce_list'),
]
