from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=34)
    email = models.EmailField()
    marks = models.IntegerField()

    def __str__(self):
        return self.name
    
