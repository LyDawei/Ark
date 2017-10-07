from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=30, default='eg. Cat Room')

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return self.name
