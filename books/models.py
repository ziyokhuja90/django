from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField()
    author = models.CharField(max_length=20)
    price = models.FloatField()
    
    
class Main(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    
class index(models.Model):
    firstP = models.TextField()
    secondP = models.TextField()
    thirdP = models.TextField()
    forthP = models.TextField()
    fifthP = models.TextField()

class Register(models.Model):
    name = models.CharField(max_length=30)
    doctorName = models.CharField(max_length=30)
    ahvol = models.CharField(max_length=30)
    phoneNumber = models.IntegerField()
    belgilar = models.TextField()
    boshlangan = models.DateField()
    