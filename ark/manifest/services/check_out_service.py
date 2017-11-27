from ..models import (CheckOut,
                      Room)
from ..services import (AnimalService)
import pdb
from datetime import (datetime,
                      timezone)


class CheckOutService:
    def __init__(self):
        self.animal_service = AnimalService()

    def get_checked_out_animal(self, animal_pk):
        '''Retrieve a checked out animal
        '''
        try:
            checked_out_animal = CheckOut.objects.get(
                animal_id=animal_pk, checked_out=True)
            return checked_out_animal
        except Exception as e:
            return None

    def get_checked_out_animals(self):
        '''Retrieve a list of all checked out animals
        '''
        try:
            checked_out_animals = CheckOut.objects.filter(checked_out=True)
            return checked_out_animals
        except Exception as e:
            return []

    def is_animal_checked_out(self, animal_pk):
        animal = self.get_checked_out_animal(animal_pk)
        if animal is None:
            return False
        return True

    def check_out_animal(self, pet_pk, room_pk, note):
        '''Check out an animal
        '''
        if self.is_animal_checked_out(pet_pk):
            raise Exception('Animal is already checked out.')

        animal = self.animal_service.get_animal_from_room(pet_pk, room_pk)
        if animal is None:
            raise Exception('Animal not in the room.')

        room = Room.objects.get(pk=room_pk)
        CheckOut.objects.create(
            animal_id=animal,
            room_id=room,
            checked_out=True,
            time_out=datetime.now(timezone.utc),
            time_in=None,
            note=note
        )

    def check_in_animal(self, pet_pk):
        '''Return a checked out animal to their assigned room.
        '''

        if not self.is_animal_checked_out(pet_pk):
            # Animal is already in the room. Just return True and ignore it.
            return True

        checked_out_animal = CheckOut.objects.get(animal_id=pet_pk)
        checked_out_animal.checked_out = False
        checked_out_animal.time_in = datetime.now(timezone.utc)
        checked_out_animal.save()
        return checked_out_animal
