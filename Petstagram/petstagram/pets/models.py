from django.db import models

from petstagram.accounts.models import UserProfile


class Pet(models.Model):
    CAT = 'Cat'
    DOG = 'Dog'
    PARROT = 'Parrot'
    UNKNOWN = 'Unknown'

    PET_TYPES = (
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown')
    )
    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6, blank=False)
    age = models.PositiveIntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='public/images')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    like = models.CharField(max_length=6)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet.name
