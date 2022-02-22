from django.http import HttpResponse
from django.shortcuts import render
from trainapp.functions import *
import feedparser
import os
from trainapp.twitterFunc import *

def index(request):
   return render(request, "index.html")

def test(request):
  
   tweets = getTweets()

   testlist = ['asd','1q','dede', tweets]
   return render(request, "test.html", {"testlist": testlist})


def search(request):
   return render(request, "searchStation.html")

  
#@app.route('/action_Search', methods =["POST"])
def action_Search(request):
  
   searchTxt = request.GET['station']

   stations = getStationNames(searchTxt)

  #return render(request, "searchStation.html", stations=stations)
   return render(request, "searchStation.html", {"stations":stations})

def stationInfo(request):

  StationName = request.GET['station']

  entries = getStationInfo(StationName)

  return render(request,"stationInfo.html",{"entries":entries,"StationName":StationName})


def rss(request):
 NewsFeed = feedparser.parse("http://fetchrss.com/rss/6213d024c2a4f2795e6706a26213cff2590aa0520b2f7ab2.xml")

 print ('Number of RSS posts :' + str(len(NewsFeed.entries)))

 entry = NewsFeed.entries[0]
 print ('Post Title :'+entry.title)
  
 return render(request,"rss.html",{"NewsFeed": NewsFeed.entries})

