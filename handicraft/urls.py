"""handicraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  url
from django.contrib import admin
from tourism import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$',views.login, name='login'),
    url(r'^babolsar$', views.babolsar, name='babolsar'),
    url(r'^help$', views.help, name='help'),
    url(r'^register$', views.register, name='register'),
    url(r'^location$', views.location, name='location'),
    url(r'^constrain$', views.location, name='constrain'),
    url(r'^sus$', views.sus, name='sus'),
    url(r'^admin/', admin.site.urls),

]
