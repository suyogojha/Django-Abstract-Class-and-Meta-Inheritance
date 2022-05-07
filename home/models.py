from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True
        
class Student(CommonInfo):
    fees = models.IntegerField()
    date = None
    
class Teacher(CommonInfo):
    salary = models.IntegerField()
    
class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()