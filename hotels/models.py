from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    contact_number = models.CharField(max_length=15, blank=True)
    
    # Amenities
    has_wifi = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    has_restaurant = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_images/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Image for {self.hotel.name}"

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Image for {self.room.room_number}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking #{self.id} - {self.guest_name} - {self.room}"