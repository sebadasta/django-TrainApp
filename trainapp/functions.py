import requests
from urllib import request, parse
import xmltodict
from datetime import datetime, timedelta
from trainapp.twitterFunc import *
from trainapp.pushNotifications import *
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
  # Get TW environment variables & replace them with empty string if no Env Variable is missing
  TW_SEARCH_RELEVANT_STRING = os.environ.get('TW_SEARCH_RELEVANT_STRING')
  TW_SEARCH_NON_RELEVANT_STRING = os.environ.get('TW_SEARCH_NON_RELEVANT_STRING')

  TW_SEARCH_RELEVANT_STRING = "" if TW_SEARCH_RELEVANT_STRING is None else TW_SEARCH_RELEVANT_STRING
  TW_SEARCH_NON_RELEVANT_STRING = "" if TW_SEARCH_NON_RELEVANT_STRING is None else TW_SEARCH_NON_RELEVANT_STRING
  
  
  sendPushNotification = False
  matchedText = ""
  
  tweets = json.loads(getTweets())

  for tweet in tweets['data'][:2]:
    
    tweet["created_at"] = dateFormatter(tweet["created_at"])

    importantText = re.search("\W*("+TW_SEARCH_RELEVANT_STRING+")\W*", tweet["text"], re.IGNORECASE)
    notRelevantText = re.search("\W*("+TW_SEARCH_NON_RELEVANT_STRING+")\W*", tweet["text"], re.IGNORECASE)

    
    if tweet["created_at"] > datetime.now() - timedelta(minutes=10) and importantText is not None and notRelevantText is None:
      
      sendPushNotification = True
      matchedText = tweet["text"]
      break

  if sendPushNotification:
    
    send_PushNotification(matchedText)
    
    print("Notification Sent \n")
    print("For Text: /n")
    print(matchedText)
    
  else:
    print("No Notification Sent")
      
    
  
def Alexa_getStationInfo(slot):
  #<Direction>Northbound</Direction>
  data = getStationInfo('KBRCK')

  if slot == "norte":  
    direction = "Northbound"

  elif slot == "sur":
        direction = "Southbound"

  trains_inStation = [row for row in data if row["Direction"]== direction]

  Speech = Alexa_StationInfo_createSpeech(trains_inStation)
      
  return Speech

def Alexa_StationInfo_createSpeech(data):
  
  speech = ""

  for train in data:

    if train['Lastlocation'] == None:
      lastLocation = "está en el limbo"
      
    else:
      lastLocation = train['Lastlocation']
      lastLocation = lastLocation.replace("Arrived", "Llegó a")
      
      lastLocation = lastLocation.replace("Departed", "Salió de ")
      
    
    speech = speech + " " + \
             "Tren a " + train['Destination'] + " " + \
             "en " + str(train['Duein']) + " minutos. " +\
             "el tren " + lastLocation + ". "
  
  return speech
