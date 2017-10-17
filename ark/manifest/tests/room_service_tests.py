from django.test import TestCase
from ..services import RoomService
import pdb


class RoomServiceTest(TestCase):
    def setUp(self):
        self.room_service = RoomService()

    def test_create_get_room(self):
        """ Test creating the room using the service layer.
        """
        self.room_service.create_room('test_room')
        room = self.room_service.get_room(name='test_room')
        self.assertTrue(room is not None)

        self.assertRaises(Exception, self.room_service.get_room)
