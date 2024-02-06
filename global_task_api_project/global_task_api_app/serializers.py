from rest_framework import serializers
from .models import Person, Vehicle, Officer

class PersonSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Person
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Vehicle
        fields = '__all__'

class OfficerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Officer
        fields = '__all__'
