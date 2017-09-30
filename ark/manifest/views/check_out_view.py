from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import CheckOut
from ..serializers import CheckoutSerializer
import pdb


@api_view(['GET'])
def get_checked_out_animals(req):
    all_checked_out_animals = CheckOut.objects.all()
    serializer = CheckoutSerializer(all_checked_out_animals, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def post_check_out_animal(req):
#     data = {
#         'id': req.body.data.get('id'),
#         'note': req.body.data.get('note')
#     }
#     serializer = CheckoutSerializer(data=data)
#     if serializer.is_valid:
#         is_animal_in_room = 
#         CheckOut.objects.create(
#             animal_id = data['id'],
            
#         )
#     return Response({})
