from django.db import models
from .animal import Animal
from .room import Room
import pdb


class AnimalToRoom(models.Model):
    animal = models.ForeignKey(Animal)
    room = models.ForeignKey(Room)

    def __str__(self):
        room = Room.objects.get(id=self.room.pk)
        animal = Animal.objects.get(id=self.animal.pk)

        return f'{room}: {animal}'
