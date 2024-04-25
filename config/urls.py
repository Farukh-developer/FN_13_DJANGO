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
        color: blue;
    }
  </style>
    </head>
    <body>
        <div>
            <h1 style="color:blue; text-align:center"> Welcome to telegram </h1>
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
        <div>:
            <h1 style="color: blue; text-align:center">
                Welcome to whatsapp
            </h1>
            <img float:left; src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30%" alt="">
        <p style="background-color: burlywood; font-size: 20px; float:right;">
            More than 2 billion people in over 180 countries use WhatsApp1 to stay in touch with <br>
            friends and family, anytime and anywhere. WhatsApp is free2 and offers simple, secure, reliable messaging and calling,<br>
             available on phones all over the world. And yes, the name WhatsApp is a pun on the phrase What's Up.
        </p>
        </div>
    </body>
</html>""")

def facebook(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: blue;
    }
     .hell{
        color: blueviolet;
        font-size: 30px;
    }
  </style>
    </head>
    <body>
        <div>:
            <h1 style="color: blue; text-align:center">
                Welcome to Facebook
            </h1>
            <img src="https://upload.wikimedia.org/wikipedia/en/0/04/Facebook_f_logo_%282021%29.svg"  width="300px" alt="There is a picture">
        <p class="hell">
            Facebook can be accessed from devices with Internet connectivity, such as personal computers, tablets and smartphones. After registering, <br>
             users can create a profile revealing information about themselves. They can post text, <br>
             photos and multimedia which are shared with any other users who have <br>
             agreed to be their friend or, with different privacy settings, publicly. <br>
             Users can also communicate directly with each other with Messenger, join common-interest groups, and receive notifications on the activities of their Facebook friends and the pages they follow. <br>
The subject of numerous controversies, Facebook has often been criticized over issues such as user privacy (as with the Cambridge Analytica data scandal), political manipulation (as with the 2016 U.S. elections) and mass surveillance. <br>
 Facebook has also been subject to criticism over psychological <br>
effects such as addiction and low self-esteem, and various controversies over content such as fake news, conspiracy theories, copyright infringement, and hate speech.[
        </p>
        </div>
    </body>
</html> """) 

def linkedin(request):
    return HttpResponse(""" <!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: darkgray;
    }
    .hell{
        color: blueviolet;
        font-size: 30px;
    }
  </style>
    </head>
    <body>
        <div>:
            <h1 style="color: blue ; text-align:center">
                Welcome to Linkeedin
            </h1>
            <img src="https://ru.wikipedia.org/wiki/SVG#/media/Файл:SVG_Logo.svg" alt="There is a picture">
        <p class="hell">
            About us
Founded in 2003, LinkedIn connects the world's professionals to make them more productive and successful. <br>
With more than 1 billion members worldwide, including executives from every Fortune 500 company, LinkedIn is the world's largest <br>
professional network. The company has a diversified business model with revenue coming from Talent Solutions,<br>
 Marketing Solutions, Sales Solutions and Premium Subscriptions products. <br>
Headquartered in Silicon Valley, LinkedIn has offices across the globe..
        </p>
        </div>
    </body>
</html> """)

def microsoft(request):
    return HttpResponse("""<!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: darkgray;
    }
    .hell{
        color: blueviolet;
        font-size: 30px;
    }
  </style>
    </head>
    <body>
        <div>
            <h1 style="color: blue ; text-align:center">
                Welcome to Microsoft
            </h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg" width='400px' alt="There is a picture">
        <p class="hell">
            Microsoft Corporation is an American multinational corporation and technology company headquartered in Redmond, <br>
            Washington.[2] Microsoft's best-known software products are the Windows line of operating systems, the Microsoft 365 <br>
            suite of productivity applications, and the Edge web browser. Its flagship hardware products are the Xbox video game <br>
             consoles and the Microsoft Surface lineup of touchscreen personal computers. Microsoft ranked No. 14 in the 2022 Fortune 500 rankings <br>
              of the largest United States corporations by total revenue;[3] and it was the world's largest software maker by revenue in 2022 according to Forbes Global 2000. <br>
               It is considered one of the Big Five American information technology companies,<br>
             alongside Alphabet (parent company of Google), Amazon, Apple, and Meta (parent company of Facebook).
        </p>
        </div>
    </body>
</html>  """)

def noname(request):
    return HttpResponse("""<h1> Hello World </h1>  """)

def twitter(request):
    return HttpResponse(""" <!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: darkgray;
    }
    .hell{
        color: blueviolet;
        font-size: 30px;
    }
  </style>
    </head>
    <body>
        <div>
            <h1 style="color: blue ; text-align:center">
                Welcome to twitter
            </h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg" width='350px' alt="There is a picture">
        <p class="hell">
            X («Экс»), обычно именуемая прежним названием «Тви́ттер» (англ. Twitter)[7][8], — американская социальная сеть. <br>
            br Это пятый по посещаемости сайт в мире и одна из крупнейших социальных сетей с 550 млн пользователей ежемесячно. <br>

В X пользователи публикуют и взаимодействуют с сообщениями, известными как «твиты». X также включает прямой обмен личными сообщениями, видео- и аудиозвонки, <br>
 закладки, списки и сообщества, а также аудиокомнаты — Spaces. <br>


Сервис предоставляется компанией X Corp.[11] — преемницей Twitter, Inc., которая базировалась <br>
 в Сан-Франциско, Калифорния, и имела более 26 офисов по всему миру[12]. Первоначально твиты были ограничены 140 символами,<br>
 но в 2017 году ограничение было удвоено до 280 для большинства языков[13]. <br>
 Аудио- и видеотвиты остаются ограниченными 140 секундами для большинства аккаунтов.
        </p>
        </div>
    </body>
</html> """)

def youtube(request):
    return HttpResponse(""" <!DOCTYPE html>
<html>
    <head>
  <style>
    #hello{
        color: darkgray;
    }
    .hell{
        color: blueviolet;
        font-size: 30px;
    }
  </style>
    </head>
    <body>
        <div>
            <h1 style="color: blue ; text-align:center">
                Welcome to YouTube
            </h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" width="350px" alt="There is a picture">
        <p class="hell">
            YouTube
Изображение логотипа
URL	youtube.com
Коммерческий	да
Тип сайта	видеохостинг
Регистрация	бесплатно
Язык (-и)	многоязычный
Посещаемость	2,5 млрд активных пользователей в месяц[1]
Язык программирования	Python
Go
Расположение сервера	 США, Сан-Бруно, Калифорния
Владелец	Google (с 2006 года)
Создатель	Стив Чен 
Чад Хёрли
Джавед Карим
Начало работы	14 февраля 2005
Текущий статус	функционирует
Число сотрудников	▲ 2000+ чел. (2019)[2]
Слоган	Broadcast Yourself
Страна	
 США
Логотип Викисклада Медиафайлы на Викискладе
YouTube (МФА: [ˈjuːt(j)uːb][3], юту́б[4], ютью́б[4]) — американский видеохостинг. <br>
 Сервис основан в 2005 году, c октября 2006 года принадлежит компании Google. <br>
  YouTube стал популярнейшим видеохостингом и вторым сайтом в мире по количеству посетителей[5]. <br>
   На 2020 год у YouTube более 2,5 млрд ежемесячных пользователей, которые ежедневно просматривают <br>
   более 1 млрд часов видео[6]. На 2021 год на сервисе насчитывалось в общей сложности около 14 млрд роликов. <br>


Бизнес-модель YouTube предполагает доход от рекламы и платного контента. <br>
 Также существует опция YouTube Premium — платная подписка для просмотра роликов без рекламы. <br>
  YouTube интегрирован в AdSense от Google, что позволяет зарабатывать как YouTube, так и создателям контента. <br>
   В 2022 году годовой доход YouTube от рекламы составил 29,2 млрд долларов[7]. <br>

С момента приобретения компанией Google, YouTube вышел за рамки основного сайта и обзавёлся приложениями <br>
 для мобильных и других платформ. Большая часть контента на YouTube создаётся пользователями, <br>
  профессионалы из которых получили название «ютуберы». Известные СМИ и развлекательные компании также создают <br>
   и развивают свои каналы на YouTube, чтобы охватить бо́льшую аудиторию.
        </p>
        </div>
    </body>
</html>""")

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
