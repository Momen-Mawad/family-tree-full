from django.db import models
from django.contrib.auth.models import User

class familyData(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first = models.CharField(max_length=20, blank=True, null=True)
    second = models.CharField(max_length=20, blank=True, null=True)
    third = models.CharField(max_length=20, blank=True, null=True)
    last = models.CharField(max_length=20, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    partner = models.CharField(max_length=20, blank=True, null=True)
    img = models.IntegerField(blank=True, null=True)

class accessRecord(models.Model):
    name = models.ForeignKey(familyData, on_delete=models.DO_NOTHING)
    date = models.DateField()

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username