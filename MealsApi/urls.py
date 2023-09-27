from django.urls import path
from MealsApi import views

urlpatterns = [
    path('', views.MealsApi , name="MealsApi")
    
]