from rest_framework import serializers
from .models import Person, Vehicle, Officer
import re

class PersonSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Person
        fields = '__all__'

    def validate(self, data): 
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, data['email']) is None:
            raise serializers.ValidationError("Invalid email")


class VehicleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Vehicle
        fields = '__all__'

class OfficerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Officer
        fields = '__all__'
