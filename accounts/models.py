from datetime import datetime,timedelta
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Department = models.CharField(max_length=10)
    adm_number = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.Department)+']' + " ["+str(self.adm_number)+']'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    copies = models.IntegerField()
    publication = models.CharField(max_length=255)
    pub_name = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)
    Date_added = models.DateField()
    status = models.CharField(max_length=255)


    def __str__(self):
        return str(self.title) + " ["+str(self.isbn)+']'

def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)