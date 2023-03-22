from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete-all/', views.delete_all, name='delete-all'),
    path('delete-ind/<int:id>', views.delete_individual, name='delete-ind'),
    path('edit/<int:id>', views.edit, name='edit')
]