from django.test import TestCase, Client
from ..models import Animal
from ..models import Room
from ..models import CheckOut
from ..models import AnimalToRoom
from rest_framework import status
from django.urls import reverse
from ..serializers import CheckoutSerializer
import datetime
import json
import pdb


class CheckOutTests(TestCase):
    client = Client()

    def setUp(self):
        # Define Animal
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

        # Define Room
        self.adult_room = Room.objects.create(name='Adult Cat Room')
        # Set animal to the room
        self.animal_to_room = AnimalToRoom.objects.create(
            animal=Animal.objects.get(pk=self.test_cat.pk),
            room=Room.objects.get(pk=self.adult_room.pk))

        # Checkout animal
        self.checked_out_animal = CheckOut.objects.create(
            animal_id=Animal.objects.get(pk=self.test_cat.pk),
            room_id=AnimalToRoom.objects.get(pk=self.animal_to_room.pk),
            checked_out=True,
            time_out=datetime.datetime.now(),
            time_in=None,
            note='Checked out for sleep over.'
        )

    def test_get_checked_out_animals(self):
        response = self.client.get(reverse('get_checked_out_animals'))
        checked_out_animals = CheckOut.objects.all()
        serializer = CheckoutSerializer(checked_out_animals, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
