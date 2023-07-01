from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('logout/', views.logout, name="logout"),
]
