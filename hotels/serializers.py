from rest_framework import serializers
from .models import Hotel, Room, Booking

class HotelSerializer(serializers.ModelSerializer):
    amenities = serializers.SerializerMethodField()
    
    class Meta:
        model = Hotel
        fields = [
            'id', 'name', 'location', 'description', 
            'price_per_night', 'contact_number', 'amenities'
        ]
    
    def get_amenities(self, obj):
        amenities = []
        if obj.has_wifi:
            amenities.append("WiFi")
        if obj.has_pool:
            amenities.append("Swimming Pool")
        if obj.has_restaurant:
            amenities.append("Restaurant")
        if obj.has_parking:
            amenities.append("Parking")
        return amenities

class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name')
    hotel_location = serializers.CharField(source='hotel.location')
    
    class Meta:
        model = Room
        fields = [
            'id', 'room_number', 'room_type', 'price_per_night',
            'capacity', 'is_available', 'hotel_name', 'hotel_location'
        ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'room', 'guest_name', 'guest_email', 
            'guest_phone', 'check_in_date', 'check_out_date',
            'total_price', 'status', 'created_at'
        ]