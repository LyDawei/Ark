from ..models import Animal
from ..models import AnimalToRoom


def get_all_animals():
    return Animal.objects.all()


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
