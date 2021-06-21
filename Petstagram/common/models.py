from django.db import models
from django.utils import timezone

from accounts.models import UserProfile
from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

