from django.test import TestCase, Client
from ..models import Animal
from ..models import AnimalToRoom
from ..models import Room
from rest_framework import status
from django.urls import reverse
from ..serializers import AnimalSerializer
from ..services import AnimalService, RoomService
import datetime
import json
import pdb


class AnimalTests(TestCase):
    client = Client()

    def setUp(self):
        AnimalService.create_animal(
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
            pet_id='4356',
        )

        Animal.objects.create(
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
            pet_id='4356',
        )

        Animal.objects.create(
            name='Ben',
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
            pet_id='4357',
        )

        Animal.objects.create(
            name='Jane',
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
            pet_id='4357',
        )

        Room.objects.create(
            name='Adult Cat Room'
        )

        Room.objects.create(
            name='Senior Cat Room'
        )

        AnimalToRoom.objects.create(
            animal=Animal.objects.get(name='Cookie'),
            room=Room.objects.get(name='Senior Cat Room')
        )

        AnimalToRoom.objects.create(
            animal=Animal.objects.get(name='Georgie'),
            room=Room.objects.get(name='Adult Cat Room')
        )

        AnimalToRoom.objects.create(
            animal=Animal.objects.get(name='Ben'),
            room=Room.objects.get(name='Adult Cat Room')
        )

        AnimalToRoom.objects.create(
            animal=Animal.objects.get(name='Jane'),
            room=Room.objects.get(name='Adult Cat Room')
        )

    def test_get_animals(self):
        response = self.client.get(reverse('get_animals'))

        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_animal(self):
        cookie_pk = Animal.objects.get(name='Cookie').pk
        response = self.client.get(
            reverse('get_animal', kwargs={'pk': cookie_pk}))
        animal = AnimalService.get_animal(cookie_pk)
        serializer = AnimalSerializer(animal)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_animal_from_room(self):
        """
            Test getting all animals that belong to a room
        """
        room_id = Room.objects.get(name='Adult Cat Room').pk
        response = self.client.get(
            reverse('get_animals_in_room', kwargs={'room': room_id})
        )

        animals_in_room = Animal.objects.filter(animaltoroom__room=room_id)
        serializer = AnimalSerializer(animals_in_room, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(3, len(response.data))

        room_id = Room.objects.get(name='Senior Cat Room').pk
        response = self.client.get(
            reverse('get_animals_in_room', kwargs={'room': room_id})
        )

        animals_in_room = Animal.objects.filter(animaltoroom__room=room_id)
        serializer = AnimalSerializer(animals_in_room, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(1, len(response.data))
