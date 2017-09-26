from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Animal
from ..serializers import AnimalSerializer


@api_view(['GET'])
def get_animal(req, pk):
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AnimalSerializer(animal)
    if req.method == 'GET':
        return Response(serializer.data)


@api_view(['GET'])
def get_animals(req):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)
