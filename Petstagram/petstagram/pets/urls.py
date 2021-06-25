from django.urls import path

from petstagram.pets.views import AllPets, CreatePet, DeletePet, PetDetails, EditPet, CommentCreate, PetLike

urlpatterns = [
    path('', AllPets.as_view(), name='all pets'),
    path('create/', CreatePet.as_view(), name='create pet'),
    path('details/<int:pk>', PetDetails.as_view(), name='pet details'),
    path('comment/<int:pk>', CommentCreate.as_view(), name='comment'),
    path('like/<int:pk>', PetLike.as_view(), name='like pet'),
    path('edit/<int:pk>', EditPet.as_view(), name='edit pet'),
    path('delete/<int:pk>', DeletePet.as_view(), name='delete pet'),
]
