"""
Definition of models.
"""

from django.db import models

# Create your models here.

class userAccount(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField(max_length=100,unique=True)
    password =  models.BinaryField(max_length=512)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    #birthday = models.DateField()
    profileText = models.CharField(max_length=1000)
    test = models.CharField(max_length=100)
    pass


class classSection(models.Model):
    classSec = models.CharField(max_length=100,primary_key=True)
    class1 = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    

class enrollment(models.Model):
    username = models.ForeignKey('userAccount',on_delete=models.CASCADE)
    classSec = models.CharField(max_length=100)