from rest_framework import serializers
from HR.models import Student
class Adddataserializer(serializers.ModelSerializer):
       class Meta:
        model = Student
        fields = ['id', 'fullname', 'agelimit']