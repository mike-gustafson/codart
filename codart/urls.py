from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('dart_like/<int:pk>/', views.dart_like, name='dart_like'),
    path('dart_dislike/<int:pk>/', views.dart_dislike, name='dart_dislike'),
    path('delete_dart/<int:pk>/', views.delete_dart, name='delete_dart'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('edit_dart/<int:pk>/', views.edit_dart, name='edit_dart'),
    path('fetch-news/', views.fetch_news, name='fetch-news'),
    path('404/', views.error_404, name='error_404', kwargs={'exception': Exception()}),
]

handler404 = 'codart.views.error_404'