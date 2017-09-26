from django.test import TestCase, Client
from ..models import Animal
from rest_framework import status
from django.urls import reverse
from ..serializers import AnimalSerializer
import datetime
import json


class AnimalTests(TestCase):
    client = Client()

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

        self.test_cat = Animal.objects.create(
            name='Georgie',
            birth_date=datetime.date(2014, 1, 1),
            is_female=False,
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

        # self.default_cat = Animal.objects.create()

    # def test_default_cat_model_values(self):
    #     cat = Animal.objects.get(pet_id=0)
    #     self.assertEqual(cat.name, 'Jane')
    #     self.assertEqual(cat.animal, 'Cat')
    #     self.assertEqual(cat.birth_date, datetime.date.today())
    #     self.assertEqual(cat.is_female, True)
    #     self.assertEqual(cat.joined, datetime.date.today())
    #     self.assertEqual(cat.personal_history, 'Stray')
    #     self.assertEqual(cat.preferences_cats, 'It\'s a possibility!')
    #     self.assertEqual(cat.declawed, False)
    #     self.assertEqual(cat.spay_neuter, True)
    #     self.assertEqual(cat.health, 'Good')

    def test_get_animals(self):
        response = self.client.get(reverse('get_animals'))

        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_animal(self):
        response = self.client.get(
            reverse('get_animal', kwargs={'pk': self.test_cat.pk}))
        animal = Animal.objects.get(pk=self.test_cat.pk)
        serializer = AnimalSerializer(animal)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
