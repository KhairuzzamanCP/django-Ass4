from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.showtask, name= 'show_task'),
    path('delete/<int:id>', views.delete, name= 'delete_task'),
    path('edit/<int:id>', views.edit, name= 'edit_task'),
    path('add/', views.add, name= 'add_task'),
    
]
