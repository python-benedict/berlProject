from django.db import models

# Create your models here.

class DetailedUser(models.Model):
    fullName    = models.CharField(max_length=100)
    email       = models.EmailField()
    studentId   = models.IntegerField()
    gender      = models.CharField(max_length=6)
    room_choosing_status    = models.CharField(max_length=3)
    bio         = models.TextField()

    def __str__(self):
        return self.fullName

class Room(models.Model):
    name    = models.TextField()
    bookings= models.ManyToManyField(DetailedUser, blank=True)

    def __str__(self):
        return self.name



