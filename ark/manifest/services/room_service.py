from ..models import Room
from ..models import AnimalToRoom
from ..models import Animal


class RoomService:
    def create_room(name):
        Room.objects.create(name=name)

    def get_room(room_id=None, name=None):
        if name is not None:
            return Room.objects.get(name=name)
        elif room_id is not None:
            return Room.objects.get(pk=room_id)
        else:
            raise Exception('One of two parameters is required.')
        
