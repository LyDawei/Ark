from django.db import models
from .animal import Animal
from .room import Room


class AnimalToRooms(models.Model):
    animal_id = models.ForeignKey(Animal)
    room_id = models.ForeignKey(Room)
