from django.urls import path
from petstagram.common.views import HomeView

urlpatterns = [
    # path('', landing_page, name='home'),
    path('', HomeView.as_view(), name='home'),
]
