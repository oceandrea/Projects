from django.urls import path

from petstagram.api.views import AllPetsApiView, PetDetailsApiView

urlpatterns = [
    path('pets/', AllPetsApiView.as_view(), name='all pets api'),
    path('pets/<int:pk>', PetDetailsApiView.as_view(), name='pet details'),
]
