from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/<str:pk>/', views.post, name='post'),
    path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),
    path('update-comment/<str:pk>/', views.update_comment, name='update-comment'),
]
