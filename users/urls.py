from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_page, name='register'),
    path('create-spending/', views.create_spending, name='create-spending'),
    path('delete-spending/<str:pk>', views.delete_spending, name='delete-spending')
]
