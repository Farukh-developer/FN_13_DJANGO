"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
def wikipedia(request):
    return HttpResponse("""<h1 style="color: red; text-align: center; "> Wikipedi history </h1>
<imag style = "height:400px; width:400px; float:left; width: 30%" src=""
<p> The period of events before the invention of writing systems is considered prehistory.<br>
"History" is an umbrella term comprising past events as well as the memory, discovery, collection,<br>
organization, presentation, and interpretation of these events. Historians seek knowledge of the past using<br>
historical sources such as written documents, oral accounts, art and material artifacts, and ecological markers.<br>
History is incomplete and still has debatable mysteries. </p>""")
def instagram(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
    <head>
        
    </head>
    <body>
        <h1 style="color: cadetblue; text-align:center">
            Information for instagram
        </h1>
        <h3 style="color:blue; text-align:center">
            Let's gooo
        </h3>
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" width="100px" alt="Picture" >
        <p style="color: blueviolet ;">
            Instagram is a free photo and video sharing app available on iPhone and Android. <br>
            People can upload photos or videos to our service and share them with their followers or with a select group of friends. <br>
             They can also view, comment and like posts shared by their friends on Instagram.
        </p>
    </body>
</html>

 """)

def telegram(request):
    return HttpResponse(""" <!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: darkgray;
    }
  </style>
    </head>
    <body>
        <div>
            <h1 style="color:blueviolet; text-align:center"> Welcome to telegram </h1>
            <img src=" https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="200px" alt="hello">
        <p id="hello">
            Telegram, cloud-based messaging app owned by Russian entrepreneurs <br>
             Pavel and Nikolai Durov. Telegram users can exchange text messages, hold voice calls, <br>
              share files, join groups of up to 200,000 members, and subscribe to public broadcast channels.
        </p>
        </div>
    </body>
</html> """)

def whatsapp(request):
    return HttpResponse(""" <h1> </h1>""")

def facebook(request):
    return HttpResponse(""" <h1> </h1>""")

def linkedin(request):
    return HttpResponse(""" <h1> </h1> """)

def microsoft(request):
    return HttpResponse(""" <h1> </h1> """)

def noname(request):
    return HttpResponse("""  """)

def twitter(request):
    return HttpResponse(""" <h1></h1> """)

def youtube(request):
    return HttpResponse("""<h1> </h1>""")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wikipediya',wikipedia),
    path('instagram',instagram),
    path('telegram',telegram),
    path('whatsapp',whatsapp),
    path('facebook',facebook),
    path('linkedin',linkedin),
    path('microsoft',microsoft),
    path('noname',noname),
    path('twitter',twitter),
    path('youtube',youtube)
    
]
