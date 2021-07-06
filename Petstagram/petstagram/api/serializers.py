from rest_framework import serializers
from petstagram.pets.models import Pet


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        # exclude = ('user',)
        fields = '__all__'
