from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Person, Officer, Vehicle, Infraction
from .serializers import OfficerSerializer, PersonSerializer, VehicleSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class PaginationClass(pagination.PageNumberPagination):
    permission_classes = [AllowAny]
    page_size = 10 
    page_size_query_param = 'page_size'

class PersonViewSet(viewsets.ModelViewSet): 
    permission_classes = [AllowAny]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    pagination_class = PaginationClass

class VehicleViewSet(viewsets.ModelViewSet): 
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer 
    pagination_class = PaginationClass

class OfficerViewSet(viewsets.ModelViewSet): 
    permission_classes = [AllowAny]
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer 
    pagination_class = PaginationClass

class LoginView(APIView): 
    def post(self, request):
        if request.method == 'POST':
            try:
                name = request.data.get('name')
                password = request.data.get('password')
                officer = Officer.objects.get(name=name)
                if officer.check_password(password): 
                    login(request, officer)
                    refresh = RefreshToken.for_user(officer)
                    return Response({'jwt': str(refresh.access_token), 'refresh': str(refresh)})
                else: 
                    return HttpResponseBadRequest('Invalid login')
            except Officer.DoesNotExist:
                return HttpResponseBadRequest('Invalid login')


class LogoutView(APIView):
    def post(self, request):
        logout(request=request)

class CreateInfractionView(APIView): 
    permission_classes = [IsAuthenticated]

    def post(self, request): 
        officer = request.user
        plate = request.data.get('plate')
        timestamp = request.data.get('timestamp')
        comments = request.data.get('comments')
        if(plate is None or timestamp is None or comments is None):
            return HttpResponseBadRequest('There are missing params')
        
        
        try:
            vehicle = Vehicle.objects.get(plate=plate)
        except Vehicle.DoesNotExist:
            return HttpResponseNotFound('Vehicle does not exist')

        Infraction.objects.create(officer=officer, plate=vehicle, timestamp=timestamp, comments=comments)
        
        return Response('Infraction created')