from ..models import Room
from ..models import AnimalToRoom
from ..models import Animal


class RoomService:
    def create_room(name):
        Room.objects.create(name=name)
