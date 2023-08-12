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


    
class Email(models.Model):
    email = models.EmailField()



class Image(models.Model):
    rasm = models.ImageField(upload_to='rasmlar')
    
    
class Hero(models.Model):
    slider = models.ImageField(upload_to='rasmlar')


class About(models.Model):
    about = models.ImageField(upload_to='rasmlar')
    
class Team(models.Model):
    team1 = models.ImageField(upload_to='rasmlar')
    team2 = models.ImageField(upload_to='rasmlar')
    team3 = models.ImageField(upload_to='rasmlar')





class Blog(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    img = models.ImageField(upload_to='blog')



class Projects(models.Model):
    name =  models.CharField(max_length=30)
    muallif =  models.CharField(max_length=30)
    narxi = models.FloatField()
    miqdor = models.IntegerField()