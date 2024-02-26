from django.urls import path
from . import views

urlpatterns = [
    path('puto/', views.getData),
    
]