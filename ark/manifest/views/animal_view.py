from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..services import AnimalService
from ..serializers import AnimalSerializer
import pdb


@api_view(['GET'])
def get_animal(req, pk):
    animal_service = AnimalService()
    try:
        animal = animal_service.get_animal(pk)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AnimalSerializer(animal)

    if req.method == 'GET':
        return Response(serializer.data)


@api_view(['GET'])
def get_animals(req):
    animal_service = AnimalService()
    animals = animal_service.get_all_animals()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_animals_in_room(req, room):
    animal_service = AnimalService()
    animals = animal_service.get_animals_from_room(room)
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)
