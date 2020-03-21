"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls'))    # inlcude() function allows referencing other url patterns. Here we are referencing other polls\urls.py urlpatterns
                                       # Whenever django encounters include() function it chops off whatever part of the URL matched upto that point and sends
                                       #  the remaining string to the included URLconf for further processing
    #path('', views.index, name = 'index'),
    #path('analyze',views.analyze , name = 'analyze')
   # path('removepunc',views.removepunc, name = 'rempun'),
   # path('capitalizefirst',views.capfirst, name = 'capfirst'),
   # path('newlineremove',views.newlineremove, name = 'newlineremove'),
   # path('spaceremove',views.spaceremove, name = 'spaceremove'),
   # path('charcount',views.charcount, name = 'charcount'),

]
