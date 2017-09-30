from django.test import TestCase
from ..services import get_all_animals
from ..services import create_animal
import datetime
import pdb


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
                      pet_id=4356)

    def test_get_all_animals(self):
        actual = get_all_animals()
        expected = f'''
            Id: 4356
            Name: Cookie
        '''
        self.assertEqual(str(actual[0]), expected)
