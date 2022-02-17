from django.http import HttpResponse
from django.shortcuts import render



def index(request):
   return render(request, "index.html")

def test(request):

   testlist = ['asd','1q','dede']
   return render(request, "test.html", {"testlist": testlist})


def search(request):
   return render(request, "searchStation.html")

  

#@app.route('/action_Search', methods =["POST"])
def action_Search(request):
  
  #searchTxt = request.form.get("station")

  #stations = getStationNames(searchTxt)
  #return render(request, "searchStation.html", stations=stations)
   return render(request, "searchStation.html", stations=[])

def stationInfo(request):

  return render(request,"stationInfo")

