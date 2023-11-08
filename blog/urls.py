from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('write/', views.post_write, name='post_write'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('comment_new/<int:pk>/', views.comment_new, name='comment_new'),
]

