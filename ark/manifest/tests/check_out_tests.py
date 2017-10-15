from django.test import TestCase, Client
from ..models import (Animal,
                      Room,
                      CheckOut,
                      AnimalToRoom)
from ..services import (AnimalService,
                        RoomService,
                        CheckOutService)
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
        self.cookie = Animal.objects.create(
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
            pet_id='4359',
        )

        self.cat_georgie = Animal.objects.create(
            name='Georgie',
            birth_date=datetime.date(2010, 3, 26),
            is_female=True,
            joined=datetime.date(2015, 3, 26),
            personal_history='Pulled from high kill shelter',
            preferences_cats='No, thank you',
            preferences_dogs='No Experience',
            preferences_kids='No Experience',
            declawed=False,
            spay_neuter=True,
            health='Good, FIV+',
            pet_id='3913',
        )

        # Define Room
        self.adult_room = Room.objects.create(name='Adult Cat Room')
        # Set animal to the room
        self.animal_to_room = AnimalToRoom.objects.create(
            animal=Animal.objects.get(pk=self.cookie.pk),
            room=Room.objects.get(pk=self.adult_room.pk))

        AnimalToRoom.objects.create(
            animal=self.cat_georgie,
            room=self.adult_room
        )

        self.valid_payload = {
            'id': Animal.objects.get(name='Georgie').pk,
            'room': Room.objects.get(name='Adult Cat Room').pk,
            'note': 'Checked out for sleep over.'
        }

        self.animal_service = AnimalService()
        self.room_service = RoomService()
        self.check_out_service = CheckOutService()

    def test_get_checked_out_animals_api(self):
        # Checkout animal
        self.checked_out_animal = CheckOut.objects.create(
            animal_id=Animal.objects.get(pk=self.cookie.pk),
            room_id=self.adult_room,
            checked_out=True,
            time_out=datetime.datetime.now(),
            time_in=None,
            note='Checked out for sleep over.'
        )

        print('test_get_checked_out_animal_api')
        response = self.client.get(reverse('get_checked_out_animals'))
        checked_out_animals = CheckOut.objects.filter(checked_out=True)
        serializer = CheckoutSerializer(checked_out_animals, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)
        self.assertGreater(len(checked_out_animals), 0)

    def test_post_check_out_animal_api(self):
        # expected code: 200
        # expected result: Animal check out object logged the animal being
        # checkedout.
        # expected: Animals checked out is 1

        expected_code = status.HTTP_200_OK
        expected_animals_in_check_out = 1

        response = self.client.post(reverse('post_check_out_animal'),
                                    data=json.dumps(self.valid_payload),
                                    content_type='application/json')
        actual_animals = CheckOut.objects.all()

        self.assertEqual(expected_code, response.status_code)
        self.assertEqual(expected_animals_in_check_out, len(actual_animals))

    def test_post_double_check_out_animal_api(self):
        expected_code = status.HTTP_412_PRECONDITION_FAILED
        expected_animals_in_check_out = 1

        # Check georgie out.
        self.client.post(reverse('post_check_out_animal'),
                         data=json.dumps(self.valid_payload),
                         content_type='application/json')

        actual_animals_in_check_out = len(
            CheckOut.objects.filter(checked_out=True))

        response = self.client.post(reverse('post_check_out_animal'),
                                    data=json.dumps(self.valid_payload),
                                    content_type='application/json')

        self.assertEqual(expected_code, response.status_code)
        self.assertEqual(expected_animals_in_check_out,
                         actual_animals_in_check_out)
