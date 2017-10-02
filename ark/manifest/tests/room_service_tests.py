from django.test import TestCase
from ..services import RoomService
import pdb


class RoomServiceTest(TestCase):
    def setUp(self):
        self

    def test_create_get_room(self):
        RoomService.create_room('test_room')
        room = RoomService.get_room(name='test_room')
        self.assertTrue(room is not None)

        self.assertRaises(Exception, RoomService.get_room)
