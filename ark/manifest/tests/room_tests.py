from django.test import TestCase
from ..models.room import Room


class RoomTests(TestCase):

    def setUp(self):
        Room.objects.create(name='Adult Cat Room', status='Need\'s cleaning')
        Room.objects.create(name='Senior Cat Room', status='Clean')
        Room.objects.create(status='Dirty')
        Room.objects.create(name='Default')

    def test_room_creation(self):
        adult_cat_room = Room.objects.get(name='Adult Cat Room')
        senior_cat_room = Room.objects.get(name='Senior Cat Room')
        self.assertEqual(adult_cat_room.__str__(), 'Adult Cat Room')
        self.assertEqual(senior_cat_room.__str__(), 'Senior Cat Room')

    def test_room_default_values(self):
        dirty_cat_room = Room.objects.get(status='Dirty')
        self.assertEqual(dirty_cat_room.name, 'eg. Cat Room')

        default_cat_room = Room.objects.get(name='Default')
        self.assertEqual(default_cat_room.status, 'eg. Spotless')
