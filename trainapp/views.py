from django.http import HttpResponse
from django.shortcuts import render
from trainapp.functions import *


def index(request):
   return render(request, "index.html")

def test(request):

   testlist = ['asd','1q','dede']
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



