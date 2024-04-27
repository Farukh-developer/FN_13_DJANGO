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
from django.urls import path, include
from.views import wikipedia, instagram, telegram, whatsapp, facebook, linkedin, microsoft, noname, twitter, youtube, ilets


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls', namespace='blog')),
    path('wikipedia/',wikipedia, name="wikipedi_path"),
    path('instagram/',instagram, name='instagram_path'),
    path('telegram/',telegram, name='telegram_path'),
    path('whatsapp/',whatsapp, name='whatsapp_path'),
    path('facebook/',facebook, name='facebook_path'),
    path('linkedin/',linkedin, name='linkedin_path'),
    path('microsoft/',microsoft, name='microsoft_path'),
    path('',noname, name='noname_path'),
    path('twitter/',twitter, name='twitter_path'),
    path('youtube/',youtube, name='youtube_path'),
    path('ielts/',ilets, name='take_ilets')
]
