from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=30, default='eg. Cat Room')
    status = models.CharField(max_length=200, default='eg. Spotless')

    def __repr__(self):
        return f'Room: {self.name} Status: {self.status}'

    def __str__(self):
        return self.name
