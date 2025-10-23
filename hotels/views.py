from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>🏨 SL Hotel Booking System</h1>
    <p>Welcome to Sri Lanka Hotel Booking</p>
    <a href="/hotels/">View Hotels</a> | 
    <a href="/admin/">Admin Panel</a>
    <p>✅ Website is working!</p>
    """)

def hotel_list(request):
    return HttpResponse("""
    <h1>🏨 All Hotels</h1>
    <p>Hotels list page - Working!</p>
    <a href="/">Back to Home</a>
    """)