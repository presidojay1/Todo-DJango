from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodos),
    path('create/', views.createTodo),
    path('update/<int:id>', views.updateTodo),
    path('delete/<int:id>', views.deleteTodo),
] 