from django.urls import path

from petstagram.pets.views import show_pet_details, like_pet, AllPets, CreatePet, DeletePet, \
    PetDetails, EditPet, CommentCreate

urlpatterns = [
    # path('', pet_all, name='all pets'),
    path('', AllPets.as_view(), name='all pets'),
    # path('create/', create_pet, name='create pet'),
    path('create/', CreatePet.as_view(), name='create pet'),
    # path('details/<int:pk>', show_pet_details, name='pet details'),
    path('details/<int:pk>', PetDetails.as_view(), name='pet details'),
    path('comment/<int:pk>', CommentCreate.as_view(), name='comment'),
    path('like/<int:pk>', like_pet, name='like pet'),
    # path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('edit/<int:pk>', EditPet.as_view(), name='edit pet'),
    # path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('delete/<int:pk>', DeletePet.as_view(), name='delete pet'),
]
