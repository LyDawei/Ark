import datetime
import pdb
from django.test import TestCase
from ..services import (RoomService,
                        AnimalService)
from ..models import (Animal,
                      AnimalToRoom)


class AnimalServiceTest(TestCase):
    def setUp(self):
        AnimalService.create_animal(name='Cookie',
                                    birth_date=datetime.date(2014, 1, 1),
                                    is_female=True,
                                    joined=datetime.date(2015, 8, 21),
                                    personal_history='Stray',
                                    preferences_cats='Absolutely!',
                                    preferences_dogs='It\'s a possibility!',
                                    preferences_kids='It\'s a possibility!',
                                    declawed=False,
                                    spay_neuter=True,
                                    health='Good, FELV+',
                                    pet_id='4356')

        AnimalService.create_animal(name='Luca',
                                    birth_date=datetime.date(2010, 4, 20),
                                    is_female=True,
                                    joined=datetime.date(2015, 8, 21),
                                    personal_history='Stray',
                                    preferences_cats='No, Thank you',
                                    preferences_dogs='It\'s a possibility!',
                                    preferences_kids='It\'s a possibility!',
                                    declawed=False,
                                    spay_neuter=True,
                                    health='Good, FELV+',
                                    pet_id='0416')

        RoomService.create_room('Adult Cat Room')

    def test_get_all_animals(self):
        actual = AnimalService.get_all_animals()
        expected = f'''
            Id: 4356
            Name: Cookie
        '''
        self.assertEqual(str(actual[0]), expected)

    def test_get_animal(self):
        animal_pk = Animal.objects.get(name='Luca').pk
        actual = AnimalService.get_animal(animal_pk)
        expected = f'''
            Id: 0416
            Name: Luca
        '''
        self.assertEqual(str(actual), expected)

    def test_assign_animal_to(self):
        AnimalService.assign_animal_to_room(
            pet_pk=Animal.objects.get(pet_id='0416').pk, room_name='Adult Cat Room')

        animals_in_rooms = AnimalToRoom.objects.all()
        self.assertGreater(len(animals_in_rooms), 0)

    def test_get_animal_from_room(self):
        animal = Animal.objects.get(pet_id='0416')
        AnimalService.assign_animal_to_room(animal.pk, 'Adult Cat Room')

        actual = AnimalService.get_animal_from_room(
            pet_pk=Animal.objects.get(pet_id='0416').pk, room_name='Adult Cat Room')
        expected = f'''
            Id: 0416
            Name: Luca
        '''
        self.assertEqual(str(actual), expected)

        actual = AnimalService.get_animal_from_room(
            pet_pk=animal.pk, room_pk=4)
        self.assertEqual(str(actual), expected)

        actual = AnimalService.get_animal_from_room(pet_pk=animal.pk)
        self.assertEqual(actual, None)

    # TODO: Right a test to get all animals from a particular room.
