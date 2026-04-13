from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField()
    comments = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


