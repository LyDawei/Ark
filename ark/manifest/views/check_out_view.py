from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import CheckOut
from ..serializers import CheckoutSerializer
from ..services import (AnimalService,
                        RoomService,
                        CheckOutService)
import pdb


@api_view(['GET'])
def get_checked_out_animals(req):
    check_out_service = CheckOutService()
    all_checked_out_animals = check_out_service.get_checked_out_animals()
    serializer = CheckoutSerializer(all_checked_out_animals, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_check_out_animal(req):
    data = {
        'id': req.data.get('id'),
        'room': req.data.get('room'),
        'note': req.data.get('note')
    }
    serializer = CheckoutSerializer(data=data)
    if serializer.is_valid:
        check_out_service = CheckOutService()
        try:
            check_out_service.check_out_animal(
                pet_pk=data['id'], room_pk=data['room'], note=data['note'])
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
