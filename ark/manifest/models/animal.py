from django.db import models
from django.core.validators import MinValueValidator


class Animal(models.Model):
    ANIMAL_CHOICES = (('Cat', 'Cat'), ('Dog', 'Dog'))
    YES_NO_CHOICES = ((False, 'No'), (True, 'Yes'))
    GENDER_CHOICES = ((False, 'Male'), (True, 'Female'))
    name = models.CharField(max_length=20, default='Jane')
    animal = models.CharField(
        max_length=3, choices=ANIMAL_CHOICES, default='Cat')
    birth_date = models.DateField(auto_now=False, blank=True, null=True)
    is_female = models.BooleanField('Gender',
                                    default=True, choices=GENDER_CHOICES)
    joined = models.DateField(auto_now=False)
    personal_history = models.CharField(max_length=50, default='Stray')
    preferences_cats = models.CharField(
        max_length=40, default='It\'s a possibility!')
    preferences_dogs = models.CharField(
        max_length=40, default='It\'s a possibility!')
    preferences_kids = models.CharField(
        max_length=40, default='It\'s a possibility!')
    declawed = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    spay_neuter = models.BooleanField(default=True, choices=YES_NO_CHOICES)
    health = models.CharField(max_length=40, default='Good')
    pet_id = models.CharField(default="9999", max_length=4)
    biography = models.TextField(max_length=1000, null=True)

    def __repr__(self):
        return f'''
            Id: {self.pet_id}
            Name: {self.name}
        '''

    def __str__(self):
        return f'''
            {self.pet_id}: {self.name}, {self.animal}
        '''
