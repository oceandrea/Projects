from django.urls import path, include

from petstagram.accounts.views import RegisterView, ProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('profile/', show_profile, name='user profile'),
    # path('profile/<int:pk>/', show_profile, name='user profile'),
    path('profile/', ProfileView.as_view(), name='user profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user profile'),
    # path('register/', register, name='register'),
    path('register/', RegisterView.as_view(), name='register'),
]


from .receivers import *

