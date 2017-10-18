from django.test import TestCase
from ..models.room import Room


class RoomTests(TestCase):

    def setUp(self):
        Room.objects.create(name='Adult Cat Room')
        Room.objects.create(name='Senior Cat Room')
        Room.objects.create(name='Default')

    def test_room_creation(self):
        """ Test creating the room at the db layer.
        """
        adult_cat_room = Room.objects.get(name='Adult Cat Room')
        senior_cat_room = Room.objects.get(name='Senior Cat Room')
        self.assertEqual(adult_cat_room.__str__(), 'Adult Cat Room')
        self.assertEqual(senior_cat_room.__str__(), 'Senior Cat Room')
