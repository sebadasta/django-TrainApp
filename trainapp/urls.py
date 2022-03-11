"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

from .AlexaIntegration.DartSkill import skill
from django_ask_sdk.skill_adapter import SkillAdapter

my_skill_view = SkillAdapter.as_view(
    skill=skill)

#path('path', method.func, name='html file')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test', views.test, name ='test'),
    path('search', views.search, name ='searchStation'),
    path('stationInfo', views.stationInfo, name ='stationInfo'),
    path('action_Search', views.action_Search, name ='stationInfo'),
  path('tw_feed', views.tw_feed, name ='tw_feed'),
  path('algo', my_skill_view, name='index'),

]