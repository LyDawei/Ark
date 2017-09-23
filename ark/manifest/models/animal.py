from django.db import models
from django.core.validators import MinValueValidator

class Animal(models.Model):
    ANIMAL_CHOICES = (('Cat', 'Cat'), ('Dog', 'Dog'))
    name = models.CharField(max_length=20, default='Jane')
    animal = models.CharField(
        max_length=3, choices=ANIMAL_CHOICES, default='DOG')
    birth_date = models.DateField(auto_now=False)
    is_female = models.BooleanField(default=True)
    joined = models.DateField(auto_now=False)
    personal_history = models.CharField(max_length=50, default='Stray')
    preferences_cats = models.CharField(
        max_length=40, default='It\'s a possibility!')
    preferences_dogs = models.CharField(
        max_length=40, default='It\'s a possibility!')
    preferences_kids = models.CharField(
        max_length=40, default='It\'s a possibility!')
    declawed = models.BooleanField(default=False)
    spay_neuter = models.BooleanField(default=False)
    health = models.CharField(max_length=40, default='Good')
    pet_id = models.IntegerField(validators=[MinValueValidator(0)])

    def __repr__(self):
        return f'Id: {self.pet_id} Name: {self.name} Animal: {self.animal}'

    def __str__(self):
        return f'''
            name: {self.name}
            birth_date: {self.birthdate}
            is_female: {self.is_female}
            joined: {self.joined}
            personal_history: {self.personal_history}
            preferences_cats: {self.preferences_cats}
            preferences_dogs: {self.preferences_dogs}
            preferences_kids: {self.preferences_kids}
            declawed: {self.declawed}
            spay_neuter: {self.spay_neuter}
            health: {self.health}
            pet_id: {self.pet_id}
        '''
