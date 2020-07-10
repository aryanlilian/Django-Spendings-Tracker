from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('post/<str:pk>/', views.post, name='post'),
    path('delete_comment/<str:pk>/', views.delete_comment, name='delete_comment'),
    path('update_comment/<str:pk>/', views.update_comment, name='update_comment'),
]
