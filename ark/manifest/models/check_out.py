from django.db import models
from .animal import Animal
from .room import Room


class CheckOut(models.Model):
    animal_id = models.ForeignKey(Animal)
    room_id = models.ForeignKey(Room)
    checked_out = models.BooleanField(default=False)
    time_out = models.DateTimeField(auto_now=False)
    time_in = models.DateTimeField(auto_now=False)
    note = models.TextField(max_length=300)
