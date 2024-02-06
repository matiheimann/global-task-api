from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    plate = models.CharField(max_length=100, primary_key=True)


class Officer(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)