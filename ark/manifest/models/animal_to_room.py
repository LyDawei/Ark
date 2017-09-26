from django.db import models
from .animal import Animal
from .room import Room


class AnimalToRoom(models.Model):
    animal_id = models.ForeignKey(Animal)
    room_id = models.ForeignKey(Room)

    def __str__(self):
        return f'{self.room_id}'
