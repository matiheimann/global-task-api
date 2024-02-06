from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Person, Officer, Vehicle
from .serializers import OfficerSerializer, PersonSerializer, VehicleSerializer

# Create your views here.

class PaginationClass(pagination.PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'

class PersonViewSet(viewsets.ModelViewSet): 
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    pagination_class = PaginationClass