from django.http import HttpResponse
from django.shortcuts import render
from trainapp.functions import *
import os
from trainapp.twitterFunc import *
from scheduler import *



def index(request):
   #startScheduler()
   #checkDartIssues()
   return render(request, "index.html")

def test(request):

   tweets = json.loads(getTweets())

   for tweet in tweets['data']:
     tweet["created_at"] = dateFormatter(tweet["created_at"])
  
   return render(request, "test.html", {"tweets": tweets['data']})


def search(request):
   return render(request, "searchStation.html")

  
def action_Search(request):
  
   searchTxt = request.GET['station']

   stations = getStationNames(searchTxt)

   return render(request, "searchStation.html", {"stations":stations})

def stationInfo(request):

  StationName = request.GET['station']

  entries = getStationInfo(StationName)

  return render(request,"stationInfo.html",{"entries":entries,"StationName":StationName})


def tw_feed(request):
  
 tweets = json.loads(getTweets())
 
 for tweet in tweets['data']:
     tweet["created_at"] = dateFormatter(tweet["created_at"])

 return render(request,"tw_feed.html",{"tweets": tweets['data']})

def start_cron(request):
   startScheduler()
   return render(request, "index.html")
  