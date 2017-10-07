from django.db import models
from .animal import Animal
from .room import Room
from .animal_to_room import AnimalToRoom


class CheckOut(models.Model):
    animal_id = models.ForeignKey(Animal)
    room_id = models.ForeignKey(Room)
    checked_out = models.BooleanField(default=False)
    time_out = models.DateTimeField(auto_now=True)
    time_in = models.DateTimeField(auto_now=False, null=True)
    note = models.TextField(max_length=300, null=True)

    def __str__(self):
        return f'''
            {self.animal_id}
            {self.room_id}
            {self.checked_out}
            {self.time_out}
            {self.time_in}
            {self.note}
        '''
