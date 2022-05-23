from django.db import models

# Create your models here.
class Student(models.Model):
    fullname=models.CharField(max_length=30)
    agelimit=models.IntegerField()