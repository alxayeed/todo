from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<int:pk>/', views.updateTask, name='update'),
    path('delete_task/<int:pk>/', views.deleteTask, name='delete'),
]