from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('', views.home, name='home'),
    path('upload/', views.file_upload, name='file_upload'),
    path('files/', views.file_list, name='file_list'),
    path('logout/', views.user_logout, name='logout'),

]
