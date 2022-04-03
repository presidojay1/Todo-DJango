from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name="home"),
   path('create/', views.create, name="create"),
   path('details/<str:pk>/', views.details, name="details"),

] 