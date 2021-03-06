from django.db import models
import datetime
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    picture = models.CharField(max_length=50)
    awards = models.ManytoManyField(Awards)
    createdAt = models.DateField(default=datetime.now())
    updatedAt = models.DateField(auto_now=True)

class Award(models.Model):
    award_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    points = models.PositiveIntegerField()
    createdAt = models.DateField(default=datetime.now())
    updatedAt = models.DateField(auto_now=True)
