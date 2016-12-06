"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="reciever")
    msg_content = models.TextField(max_length=1500)
    created_at = models.TimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileText = models.CharField(max_length=1000, blank=True)
    city = models.CharField(max_length=30, blank=True)
    birthday= models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)

# SIGNALS to auto update Profile db whenever a new user is added
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class classSection(models.Model):
    classSec = models.CharField(max_length=100,primary_key=True)
    class1 = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    

class enrollment(models.Model):
    username = models.ForeignKey('Profile',on_delete=models.CASCADE)
    classSec = models.CharField(max_length=100)