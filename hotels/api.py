from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Hotel, Room, Booking
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer

@api_view(['GET'])
def api_hotel_list(request):
    """Get all hotels API"""
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_hotel_detail(request, hotel_id):
    """Get single hotel details API"""
    try:
        hotel = Hotel.objects.get(id=hotel_id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    except Hotel.DoesNotExist:
        return Response(
            {"error": "Hotel not found"}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
def api_room_list(request):
    """Get all rooms API"""
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_room_detail(request, room_id):
    """Get single room details API"""
    try:
        room = Room.objects.get(id=room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response(
            {"error": "Room not found"}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['POST'])
def api_create_booking(request):
    """Create booking API"""
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Booking created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_search_hotels(request):
    """Search hotels API"""
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    
    hotels = Hotel.objects.all()
    
    if query:
        hotels = hotels.filter(name__icontains=query)
    if location:
        hotels = hotels.filter(location__icontains=location)
    
    serializer = HotelSerializer(hotels, many=True)
    return Response({
        "query": query,
        "location": location,
        "count": hotels.count(),
        "results": serializer.data
    })