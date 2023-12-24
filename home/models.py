from django.db import models
from pyexpat import model
from statistics import mode
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Basemodel(models.Model):
     uid = models.UUIDField(default=uuid.uuid4(), editable = False, primary_key=True)
     created_at = models.DateField(auto_now_add=True)
     updated_at= models.DateField(auto_now_add=True)
     
     class Meta:
         abstract=True
     
     
     
class Amenities(Basemodel):
    amenity_name=models.CharField(max_length=50)
     
    def __str__(self) -> str:
        return self.amenity_name

     
class Hotel(Basemodel):
    hotel_name= models.CharField(max_length=80)
    hotel_price= models.IntegerField()
    hotel_description = models.TextField()
    amenities= models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)
    
    def __str__(self) -> str:
        return self.hotel_name
    
    
class HotelImages(Basemodel):
    hotel= models.ForeignKey(Hotel, related_name="hotel", on_delete=models.CASCADE)
    images= models.ImageField(upload_to="hotel")
      
      
class HotelBooking(Basemodel):
    hotel=models.ForeignKey(Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User ,related_name="user_booking", on_delete=models.CASCADE)
    start_date=models.DateField(auto_now_add=True)
    end_date= models.DateField(auto_now_add=True)
    booking_type = models.CharField(max_length=50,choices=(('Pre Paid','Pre Paid'),('Post Paid', 'Post Paid')))
     