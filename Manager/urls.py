from django.urls import path
from Manager import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.Add_food, name='add'),
]
