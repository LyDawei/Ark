from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import CheckOut
from ..serializers import CheckoutSerializer


@api_view(['GET'])
def get_checked_out_animals(req):
    all_checked_out_animals = CheckOut.objects.all()
    serializer = CheckoutSerializer(all_checked_out_animals, many=True)
    return Response(serializer.data)
