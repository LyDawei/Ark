from django.contrib import admin
from .models.animal import Animal
from .models.animal_to_room import AnimalToRoom
from .models.check_out import CheckOut
from .models.room import Room

# Register your models here.
admin.site.register(Animal)
admin.site.register(AnimalToRoom)
admin.site.register(Room)
