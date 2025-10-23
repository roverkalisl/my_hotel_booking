from django.contrib import admin
from .models import Hotel, Room, Booking, HotelImage, RoomImage

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price_per_night', 'has_wifi', 'has_pool']
    list_filter = ['location', 'has_wifi', 'has_pool', 'has_restaurant']
    search_fields = ['name', 'location']
    inlines = [HotelImageInline, RoomInline]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'hotel', 'room_type', 'price_per_night', 'is_available']
    list_filter = ['hotel', 'room_type', 'is_available']
    search_fields = ['room_number', 'hotel__name']
    inlines = [RoomImageInline]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest_name', 'room', 'check_in_date', 'check_out_date', 'status']
    list_filter = ['status', 'check_in_date', 'created_at']
    search_fields = ['guest_name', 'guest_email', 'room__hotel__name']

@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'caption']

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ['room', 'caption']