import requests
from urllib import request, parse
import xmltodict
from datetime import datetime
from trainapp.twitterFunc import *
import re
import os

Station_URL = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode="
#Station_URL="http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc="

search_URL = "http://api.irishrail.ie/realtime/realtime.asmx/getStationsFilterXML?StationText="

#Aux Vars
thisdict = {}
cleanData = {}

#gets raw data from Api
def getAPI(station):
  if station == None:
    station = "KBRCK"

  response = requests.get(Station_URL + station)

  return xmltodict.parse(response.content)


#Filters Station Data (dict_data)
def formatData(dict_data):

  try:
    
    data = dict_data["ArrayOfObjStationData"]["objStationData"]

    next_trains_inStation = [row for row in data if is_valid_Duein(row["Duein"]) <= 30]
    
  except:
    return []
    
  return next_trains_inStation
  

def is_valid_Duein(Duein_String):

  try:
    return int(Duein_String)
  except:
    return False


def getStationNames(searchTxt):
  responseData = requests.get(search_URL + searchTxt)
  
  try:
    parsedResponse = xmltodict.parse(responseData.content)
    data = parsedResponse['ArrayOfObjStationFilter']['objStationFilter']

    if (isinstance(data,list)):
      output = data
      return output
    else:
      output = []
      output.append(data)
      return output
      
  except:
    print("error")

def getStationInfo(station):

  #call func to get API Data
  dict_data = getAPI(station)

  return formatData(dict_data)

def dateFormatter(dateStr):

  try:
   return datetime.strptime(dateStr,"%Y-%m-%dT%H:%M:%S.%fZ")  
  except:
   return "Error"


def checkDartIssues():
  PUSH_KEY = os.environ.get("PUSH_KEY")
  PUSH_URL = os.environ.get("PUSH_URL")
  #bearer_token = os.environ.get("BEARER_TOKEN")

  
  tweets = getTweets()

  x = re.search("\W*(issue|delay|interruption|suspended|problem|block|cancel)\W*", tweets, re.IGNORECASE)

  data = parse.urlencode({'key': PUSH_KEY, 'title': 'Train Alert!', 'msg': 'Check Dart Twitter, something is wrong', 'event': 'Dart Issue'}).encode()
  
  req = request.Request(PUSH_URL, data=data)
  
  request.urlopen(req)
  
  #print(x.string)
  

  
