from django.db import models

from petstagram.accounts.models import UserProfile
from petstagram.pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet.name

