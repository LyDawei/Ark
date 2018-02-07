from django.db import models
from .animal import Animal


class AnimalImage(models.Model):
    animal_id = models.ForeignKey(Animal)
    image = models.FileField(upload_to='https://ark001.blob.core.windows.net/cats', blank=True)
