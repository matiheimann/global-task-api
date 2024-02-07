from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Person, Officer, Vehicle
from .serializers import OfficerSerializer, PersonSerializer, VehicleSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class PaginationClass(pagination.PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'

class PersonViewSet(viewsets.ModelViewSet): 
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    pagination_class = PaginationClass

class VehicleViewSet(viewsets.ModelViewSet): 
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer 
    pagination_class = PaginationClass

class OfficerViewSet(viewsets.ModelViewSet): 
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer 
    pagination_class = PaginationClass

class LoginView(APIView): 
    def post(self, request):
        if request.method == 'POST':
            try:
                id = request.data.get('id')
                officer = Officer.objects.get(id=id)
                token = AccessToken.for_user(officer)
                return Response({'jwt': str(token)})
            except Officer.DoesNotExist:
                return HttpResponseBadRequest('Invalid login')


def LogoutView(request):
    logout(request)