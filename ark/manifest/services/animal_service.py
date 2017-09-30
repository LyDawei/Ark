from ..models import Animal
from ..models import AnimalToRoom
from ..models import Room


def get_all_animals():
    return Animal.objects.all()


def get_animal(pet_id):
    return Animal.objects.get(pet_id=pet_id)


def get_animals_from_room(room_id):
    animals = Animal.objects.filter(animaltoroom__room_id=room_id)
    return animals


def create_animal(name, birth_date, is_female, joined,
                  personal_history, preferences_cats,
                  preferences_dogs, preferences_kids,
                  declawed, spay_neuter, health, pet_id):
    """ Creates an animal in the database. """
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


def assign_animal_to_room(pet_id, room_name):
    room = Room.objects.get(name=room_name)
    animal = Animal.objects.get(pet_id=pet_id)
    AnimalToRoom.objects.create(
        animal=animal,
        room=room
    )
    return 200


def get_animal_from_room(pet_id, room_id=None, room_name=None):
    animal = Animal.objects.get(pet_id=pet_id)
    if room_id is not None:
        animal = Animal.objects.filter(animaltoroom__room=room_id).filter(
            animaltoroom__animal=animal.pk)
    elif room_name is not None:
        room = Room.objects.get(name=room_name)
        animal = Animal.objects.filter(animaltoroom__room=room.pk).filter(
            animaltoroom__animal=animal.pk)
    else:
        animal = None
    return animal[0] if animal else None
