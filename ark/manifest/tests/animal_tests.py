from django.test import TestCase
from ..models import Animal
import datetime


class AnimalTests(TestCase):
    def setUp(self):
        self.test_cat = Animal.objects.create(
            name='Cookie',
            birth_date=datetime.date(2014, 1, 1),
            is_female=True,
            joined=datetime.date(2015, 8, 21),
            personal_history='Stray',
            preferences_cats='Absolutely!',
            preferences_dogs='It\'s a possibility!',
            preferences_kids='It\'s a possibility!',
            declawed=False,
            spay_neuter=False,
            health='Good, FELV+',
            pet_id=4356,
        )

    def test_cat_model(self):
        cat = Animal.objects.get(pet_id=4356)
        self.assertEqual(cat, self.test_cat)
