from ..models import (Animal,
                      AnimalToRoom,
                      Room,
                      CheckOut)
from .room_service import RoomService
import pdb


class AnimalService:

    def assign_animal_to_room(self, pet_pk, room_pk):
        '''Assign an animal to a room
        '''
        room = Room.objects.get(pk=room_pk)
        animal = Animal.objects.get(pk=pet_pk)
        AnimalToRoom.objects.create(
            animal=animal,
            room=room
        )

    def create_animal(self, name, birth_date, is_female, joined,
                      personal_history, preferences_cats,
                      preferences_dogs, preferences_kids,
                      declawed, spay_neuter, health, pet_id):
        ''' Creates an animal in the database.
        and returns that animal
        '''
        Animal.objects.create(
            name=name,
            birth_date=birth_date,
            is_female=is_female,
            joined=joined,
            personal_history=personal_history,
            preferences_cats=preferences_cats,
            preferences_dogs=preferences_dogs,
            preferences_kids=preferences_kids,
            declawed=declawed,
            spay_neuter=spay_neuter,
            health=health,
            pet_id=pet_id,
        )

        animal = Animal.objects.get(pet_id=pet_id)
        return animal

    def get_all_animals(self,):
        '''Get all animals from the db
        '''
        return Animal.objects.all()

    def get_animal(self, id):
        '''Get an animal
        '''
        return Animal.objects.get(pk=id)

    def get_animals_from_room(self, pk):
        '''Get all animals from a room
        '''
        animals = Animal.objects.filter(animaltoroom__room_id=pk)
        return animals

    def get_animal_from_room(self, pet_pk, room_pk=None, room_name=None):
        '''Retrieve an animal from the room
        '''
        if room_pk is not None:
            animal = Animal.objects.filter(animaltoroom__room=room_pk).filter(
                animaltoroom__animal=pet_pk)
        elif room_name is not None:
            room = Room.objects.get(name=room_name)
            animal = Animal.objects.filter(animaltoroom__room=room.pk).filter(
                animaltoroom__animal=pet_pk)
        else:
            animal = Animal.objects.filter(animaltoroom__animal=pet_pk)
        return animal[0] if animal else None
