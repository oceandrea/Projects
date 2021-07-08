from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from petstagram.api.serializers import PetsSerializer
from petstagram.pets.models import Pet


class AllPetsApiView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.userprofile)


class PetDetailsApiView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        pet = self.get_object(pk)
        serializer = PetsSerializer(pet)
        return Response(serializer.data)

    def put(self, request, pk):
        pet = self.get_object(pk)
        serializer = PetsSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pet = self.get_object(pk)
        if pet:
            pet.delete()
            return Response(status=status.HTTP_202_ACCEPTED)