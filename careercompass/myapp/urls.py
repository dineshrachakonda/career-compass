from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('field/', views.field, name = 'field'),
    path('field/course/<string>/', views.college, name = 'college')
]