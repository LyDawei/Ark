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

        self.default_cat = Animal.objects.create()

    def test_cat_model(self):
        cat = Animal.objects.get(pet_id=4356)
        self.assertEqual(cat, self.test_cat)

    def test_default_cat_model_values(self):
        cat = Animal.objects.get(pet_id=0)
        self.assertEqual(cat.name, 'Jane')
        self.assertEqual(cat.animal, 'Cat')
        self.assertEqual(cat.birth_date, datetime.date.today())
        self.assertEqual(cat.is_female, True)
        self.assertEqual(cat.joined, datetime.date.today())
        self.assertEqual(cat.personal_history, 'Stray')
        self.assertEqual(cat.preferences_cats, 'It\'s a possibility!')
        self.assertEqual(cat.declawed, False)
        self.assertEqual(cat.spay_neuter, True)
        self.assertEqual(cat.health, 'Good')
