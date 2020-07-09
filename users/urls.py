from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('create_spending/', views.create_spending, name='create_spending'),
    path('delete_spending/<str:pk>', views.delete_spending, name='delete_spending')
]
