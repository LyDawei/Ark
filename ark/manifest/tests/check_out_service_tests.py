from django.test import TestCase, Client
from ..models import (Animal,
                      Room,
                      CheckOut,
                      AnimalToRoom)
from rest_framework import status
from django.urls import reverse
from ..serializers import CheckoutSerializer
from ..services import(AnimalService,
                       RoomService,
                       CheckOutService)
import datetime
import json
import pdb


class CheckOutServiceTest(TestCase):
    def setUp(self):
        # create animals
        # create rooms
        # assign animals to rooms
        self.animal_service = AnimalService()
        self.room_service = RoomService()
        self.check_out_service = CheckOutService()

        self.cookie = self.animal_service.create_animal(
            name='Cookie',
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

        self.georgie = self.animal_service.create_animal(
            name='Georgie',
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
            pet_id='4357')

        self.adult_cat_room = self.room_service.create_room(
            name='Adult Cat Room')

        self.animal_service.assign_animal_to_room(
            pet_pk=self.cookie.pk,
            room_pk=self.adult_cat_room.pk)

        self.animal_service.assign_animal_to_room(
            pet_pk=self.georgie.pk,
            room_pk=self.adult_cat_room.pk
        )

    def test_check_out_animal_service(self):
        georgie = Animal.objects.get(name='Georgie')
        self.assertEqual(len(CheckOut.objects.all()), 0)
        self.check_out_service.check_out_animal(georgie.pk,
                                                self.room_service.get_room(
                                                    name='Adult Cat Room').pk,
                                                'At a sleep over')
        george_checked_out = CheckOut.objects.get(animal_id=georgie.pk)
        self.assertIsNotNone(george_checked_out)

    def test_double_check_out_animal_service(self):
        '''Cookie has been checked out. Check her out again.
        Expected behavior is that she cannot be checked out.
        '''
        self.checked_out_animal = CheckOut.objects.create(
            animal_id=self.cookie,
            room_id=self.adult_cat_room,
            checked_out=True,
            time_out=datetime.datetime.now(),
            time_in=None,
            note='Checked out for sleep over.'
        )

        animal_pk = self.cookie.pk
        room_pk = self.adult_cat_room.pk
        note = 'At a sleep over'
        self.assertRaises(Exception, self.check_out_service.check_out_animal,
                          animal_pk, room_pk, note)

    def test_get_all_checked_out_animals_service(self):
        self.assertEqual(
            len(self.check_out_service.get_checked_out_animals()), 0)

        self.check_out_service.check_out_animal(
            self.cookie.pk, self.adult_cat_room.pk, 'Sleep over')
        self.check_out_service.check_out_animal(
            self.georgie.pk, self.adult_cat_room.pk, 'Sleep over')

        self.assertGreater(
            len(self.check_out_service.get_checked_out_animals()), 0)

    def test_get_checked_out_animal_service(self):
        self.assertEqual(
            len(self.check_out_service.get_checked_out_animals()), 0)

        self.check_out_service.check_out_animal(
            self.cookie.pk, self.adult_cat_room.pk, 'Test')

        expected = CheckOut.objects.get(animal_id=self.cookie.pk)
        actual = self.check_out_service.get_checked_out_animal(
            animal_pk=self.cookie.pk)
        self.assertEqual(actual, expected)
