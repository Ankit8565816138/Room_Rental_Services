from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=20,null=True)
    dob = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    def _str_ (self):
        return self.user.username

class Contact_Us(models.Model):
    full_name=models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=40, null=True)
    contact = models.CharField(max_length=40, null=True)
    comment = models.CharField(max_length=40, null=True)


class Feedback(models.Model):
    full_name=models.CharField(max_length=30,null=True)
    contact_no = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    feedback = models.CharField(max_length=40, null=True)

class Room(models.Model):
    room_no = models.CharField(max_length=20,null=True,unique=True)
    price = models.CharField(max_length=30,null=True)
    r_type = models.CharField(max_length=40,null=True)
    r_image = models.FileField(null=True)
    status = models.CharField(max_length=30,null=True)

class Booking(models.Model):
    room_no = models.CharField(max_length=20,null=True)
    full_name = models.CharField(max_length=20, null=True)
    email_id = models.CharField(max_length=20, null=True)
    mobile1 = models.CharField(max_length=20, null=True)
    mobile2 = models.CharField(max_length=20, null=True)
    booking_date = models.CharField(max_length=20, null=True)
    days = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
