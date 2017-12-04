from rest_framework import serializers
from .models import Animal, CheckOut


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('pk', 'name', 'animal', 'birth_date', 'is_female', 'breed', 'joined',
                  'personal_history', 'preferences_cats', 'preferences_dogs',
                  'preferences_kids', 'declawed', 'spay_neuter', 'health',
                  'pet_id', 'biography')


class CheckoutSerializer(serializers.Serializer):
    class Meta:
        model = CheckOut
        fields = ('id', 'room', 'note')
