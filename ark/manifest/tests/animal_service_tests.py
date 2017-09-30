import datetime
import pdb
from django.test import TestCase
from ..services import (create_animal,
                        create_room,
                        get_all_animals,
                        get_animal,
                        get_animal_from,
                        get_animals_from_room,
                        assign_animal_to_room)


class AnimalServiceTest(TestCase):
    def setUp(self):
        create_animal(name='Cookie',
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

        create_animal(name='Luca',
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

        create_room('Adult Cat Room')

    def test_get_all_animals(self):
        actual = get_all_animals()
        expected = f'''
            Id: 4356
            Name: Cookie
        '''
        self.assertEqual(str(actual[0]), expected)

    def test_get_animal(self):
        actual = get_animal('0416')
        expected = f'''
            Id: 0416
            Name: Luca
        '''

    def test_assign_animal_to(self):
        actual = assign_animal_to_room(
            pet_id='0416', room_name='Adult Cat Room')
        expected = 200
        self.assertEqual(actual, expected)

    def test_get_animal_from_room(self):
        assign_animal_to_room('0416', 'Adult Cat Room')

        actual = get_animal_from_room(pet_id='0416', room_name='Adult Cat Room')
        expected = f'''
            Id: 0416
            Name: Luca
        '''
        self.assertEqual(str(actual), expected)

        actual = get_animal_from_room(
            pet_id='0416', room_id=4)
        self.assertEqual(str(actual), expected)

        actual = get_animal_from_room(pet_id='0416')
        self.assertEqual(actual, None)
