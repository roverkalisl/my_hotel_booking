from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def hotel_list(request):
    return HttpResponse("Hotels list page - Working!")