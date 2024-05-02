from django.shortcuts import render
from django.shortcuts import HttpResponse

students = [
    {"id": 1, "name": "John", "surname": "Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane", "surname": "Smith", "email": "jane.smith@example.com"},
    {"id": 3, "name": "Alice", "surname": "Johnson", "email": "alice.johnson@example.com"},
    {"id": 4, "name": "Bob", "surname": "Brown", "email": "bob.brown@example.com"},
    {"id": 5, "name": "Emily", "surname": "Williams", "email": "emily.williams@example.com"},
    {"id": 6, "name": "Michael", "surname": "Jones", "email": "michael.jones@example.com"},
    {"id": 7, "name": "Sophia", "surname": "Davis", "email": "sophia.davis@example.com"},
    {"id": 8, "name": "David", "surname": "Miller", "email": "david.miller@example.com"},
    {"id": 9, "name": "Olivia", "surname": "Wilson", "email": "olivia.wilson@example.com"},
    {"id": 10, "name": "James", "surname": "Taylor", "email": "james.taylor@example.com"}
]
def youtube(request):
    return render(request, 'youtube.html')

def facebook(request):
    return render(request, 'facebook.html')


def telegram(request):
    return render(request, 'telegram.html')

def instagram(request):
    return render(request, 'instagram.html')

def microsoft(request):
    return render(request, 'microsoft.html')

def linkeedin(request):
    return render(request, 'linkeedin.html')

def whatsapp(request):
    return render(request, 'whatsapp.html')

def wikipedia(request):
    return render(request, 'wikipedia.html')

def twitter(request):
    return render(request, 'twitter.html')

    

def find_name(request, name):
    for student in students:
        if student["name"]==name:
            return render(request,'find_all.html', context={'person':student})
    return HttpResponse(f'{name}')


def find_id(request, id):
    for student in students:
        if student["id"]==id:
            return render(request,'find_all.html',context={'person':student})
    return HttpResponse(f'{id}')

def find_email(request, email):
    for student in students:
        if student["email"]==email:
            return render(request,'find_all.html',context={'person':student})
    return HttpResponse(f'{email}')
















