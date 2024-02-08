from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    id = models.AutoField(primary_key=True)

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    plate = models.CharField(max_length=100, primary_key=True)

class CustomOfficerManager(BaseUserManager):
    def create_officer(self, password=None, **extra_fields):
        officer = self.model( **extra_fields)
        officer.set_password(password)
        officer.save(using=self._db)
        return officer

class Officer(AbstractBaseUser):
    name = models.CharField(max_length=100, unique=True)
    id = models.AutoField(primary_key=True)
    objects = CustomOfficerManager()

    USERNAME_FIELD = 'name'

class Infraction(models.Model):
    plate = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    comments = models.TextField()
    timestamp = models.CharField(max_length=100)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)