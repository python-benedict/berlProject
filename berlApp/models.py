from django.db import models

# Create your models here.

class DetailedUser(models.Model):
    fullName    = models.CharField(max_length=100)
    email       = models.EmailField()
    studentId   = models.IntegerField()
    gender      = models.CharField(max_length=6)
    roomtype    = models.CharField(max_length=100)
    room_choosing_status    = models.CharField(max_length=3)
    bio         = models.TextField()

    def __str__(self):
        return self.fullName

class MRoom1mw(models.Model):
    name = models.ManyToManyField(DetailedUser)


class MRoom2mw(models.Model):
    name = models.ManyToManyField(DetailedUser)

class MRoom3mw(models.Model):
    name = models.ManyToManyField(DetailedUser)

class MRoom4mw(models.Model):
    name = models.ManyToManyField(DetailedUser)