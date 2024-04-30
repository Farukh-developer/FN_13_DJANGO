from django.shortcuts import render

# Create your views here.
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












