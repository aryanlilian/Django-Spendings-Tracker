from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('create-spending/', views.create_spending, name='create-spending'),
    path('delete-spending/<str:pk>', views.delete_spending, name='delete-spending')
]
