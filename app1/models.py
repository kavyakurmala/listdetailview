from pyexpat import model
from statistics import mode
from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=30)
    principal = models.CharField(max_length=30)
    loc = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app1:detail",kwargs={'pk':self.pk})
        

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name