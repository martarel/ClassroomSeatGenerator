from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=20)

class ClassName(models.Model):
    name = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=20)
    def __str__(self):
        return self.name
