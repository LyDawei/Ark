from django.db import models
from .animal import Animal
from .animal_image import AnimalImage


class AnimalToImage(models.Model):
    animal_id = models.ForeignKey(Animal)
    image_id = models.ForeignKey(AnimalImage)
