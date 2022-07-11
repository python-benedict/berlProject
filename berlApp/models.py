from django.db import models

# Create your models here.
GENDER = [
    ('1', 'Male'),
    ('2', 'Female')
]


class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class DetailedUser(BaseTimeModel):
    MRoom1mw = "FOUR IN A ROOM SELF-CONTAIN WITH BALCONY KICHENNETTE"
    MRoom2mw = "TWO IN A ROOM SELF-CONTAIN WITH BALCONY KICHENNETTE"
    MRoom3mw = "TWO IN A ROOM SELF-CONTAIN WITH KITCHEN AND HALL"
    MRoom4mw = "TWO IN A ROOM SELF-CONTAIN WITH CHAMBER AND HALL"

    choose_myself = 'Manual room Selection'
    choose_for_me = 'Automatic room allocation'
    
    ROOMTYPE = [
        (MRoom1mw, MRoom1mw),
        (MRoom2mw, MRoom2mw),
        (MRoom3mw, MRoom3mw),
        (MRoom4mw, MRoom4mw)
    ]

    ROOMSTATUS = [
        (choose_myself, choose_myself),
        (choose_for_me, choose_for_me)
    ]

    fullName    = models.CharField(max_length=100)
    email       = models.EmailField()
    studentId   = models.IntegerField()
    roomtype    = models.CharField(choices=ROOMTYPE, max_length=120, blank=True)
    gender      = models.CharField(choices=GENDER, max_length=6, blank=True)
    room_choosing_status    = models.CharField(choices=ROOMSTATUS ,max_length=50)
    bio         = models.TextField()

    def __str__(self):
        return self.fullName


class Room(BaseTimeModel):
    name        = models.CharField(max_length=120)
    capacity    = models.IntegerField(default=0)
    people      = models.ManyToManyField(DetailedUser, blank=True)
    gender      = models.CharField(choices=GENDER, max_length=6, blank=True)
    full        = models.BooleanField(default=False)

    def __str__(self):
        return self.name



