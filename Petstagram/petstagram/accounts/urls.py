from django.urls import path, include
from .receivers import *
from petstagram.accounts.views import RegisterView, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='user profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
