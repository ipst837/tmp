from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.main_page, name='main'),
]
