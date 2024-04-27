from django.shortcuts import render


def wikipedia(request):
    return render(request,'wikipedia.html')

def instagram(request):
    return render(request,'instagram.html')

def telegram(request):
    return render(request,'telegram.html')
    
def whatsapp(request):
    return render(request,'whatsapp.html')

def facebook(request):
    return render(request,'facebook.html')
    
def linkedin(request):
    return render(request,'linkedin.html')

def microsoft(request):
    return render(request,'microsoft.html')

def noname(request):
    return render(request,'noname.html')

def twitter(request):
    return render(request,'twitter.html')

def youtube(request):
    return render(request,'youtube.html')
def ilets(request):
    return render(request,'ielts.html')