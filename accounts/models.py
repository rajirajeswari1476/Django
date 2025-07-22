from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
### ctreate custmoer model and inherite from AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES=[
        ('admin','Admin'),
        ('sales','sales')

    ]
    role=models.CharField(max_length=50,choices=ROLE_CHOICES,default='admin')

class Student(models.Model):
    added_by= models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    skillset = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.name



