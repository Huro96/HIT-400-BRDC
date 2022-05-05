from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Projects(models.Model):
    rate_number= models.CharField('Rates',max_length=10)
    name= models.CharField('Description',max_length=200)
    price =models.FloatField()

    def __str__(self):
        return self.name + "" + str(self.price) + " " + self.rate_number 


class UnwantedWords(models.Model):
    #number= models.IntegerField()
    name=models.CharField("Name of word",max_length=100)
    
    def __str__(self):
        return  self.name

class BlockContacts(models.Model):
    username = models.CharField('Username',max_length=25)
    word = models.CharField('Word Used',max_length=25)
    date=models.DateTimeField(default=timezone.now, blank=True)    
    def __str__(self):
        return  self.username + " " + self.word + "  " + str(self.date)

class RatesComments(models.Model):
    username = models.CharField('Username',max_length=25)
    rate =models.CharField('Rate Number',max_length=10)
    comment= models.CharField('Comment', max_length=500)
    date=models.DateTimeField("%Y-%m-%d T%H:%M", blank=True)
    
    def __str__(self):
        return self.username + "  " + self.comment + " " + str(self.date) 

class Tarrifs(models.Model):
    name=models.CharField("Description",max_length=30)
    tarrif_number = models.CharField("Tarrif Number",max_length=10)
    amount= models.FloatField()
    update_date = models.DateTimeField()
    comment= models.CharField("Reason for Price",max_length=500,blank=True)
    username= models.CharField('Changed by',max_length=25)
    
    def __str__(self):
        return self.name + "  " + str(self.amount) + "   " +  str(self.update_date) + "  "+ self.comment  + self.username
    
class Profile(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    ward = models.CharField("Ward",max_length=2,blank=True)

    def __str__(self):
        return self.username + "  " + str(self.ward)