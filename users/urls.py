from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_page, name='register'),
    path('create-spending/', views.create_spending, name='create-spending'),
    path('delete-spending/<str:pk>', views.delete_spending, name='delete-spending'),
    path('notes/', views.notes, name='notes'),
    path('create-note/', views.create_note, name='create-note'),
    path('delete-note/<str:pk>', views.delete_note, name='delete-note'),
    path('tasks/<str:pk>', views.tasks, name='tasks'),
    path('delete-task/<str:pk>', views.delete_task, name='delete-task'),
    path('update-task/<str:pk>', views.update_task, name='update-task'),
    path('add-budget/', views.add_budget, name='add-budget'),
    path('archive/', views.archive, name='archive')
]
