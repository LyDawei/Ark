from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import CheckOut
from ..serializers import CheckoutSerializer
from ..services import (AnimalService,
                        RoomService)
import pdb


@api_view(['GET'])
def get_checked_out_animals(req):
    animal_service = AnimalService()
    all_checked_out_animals = animal_service.get_checked_out_animals()
    serializer = CheckoutSerializer(all_checked_out_animals, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_check_out_animal(req):
    data = {
        'id': req.body.data.get('id'),
        'room_id': req.body.data.get('room_id'),
        'note': req.body.data.get('note')
    }
    serializer = CheckoutSerializer(data=data)
    if serializer.is_valid:
        animal_service = AnimalService()
        animal = animal_service.get_animal_from_room(
            pet_pk=data['id'], room_pk=data['room_id'])
        
    return Response({})
