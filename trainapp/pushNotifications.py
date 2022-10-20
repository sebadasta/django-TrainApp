import requests
from urllib import request, parse
import re
import os
from flagsmith import Flagsmith;


flagsmith = Flagsmith(
    environment_key = os.environ.get("FLAGS_ENV")
)


#SIMPLE PUSH IO Credentials (Just 100 Push Notifications per month)
PUSH_KEY = os.environ.get("PUSH_KEY")
PUSH_URL = os.environ.get("PUSH_URL")

#PUSHED.CO Credentials (1000 Push Notifications per month)
PUSH_APP_KEY = os.environ.get("PUSH_APP_KEY")
PUSH_APP_SECRET = os.environ.get("PUSH_APP_SECRET")



def send_PushNotification(matchedText):

    # The method below triggers a network request
    flags = flagsmith.get_environment_flags()
    
    # Check if enable_notifications is enabled
    pushNotifications_is_enabled = flags.is_feature_enabled("enable_notifications")
    simplePush_isEnabled = flags.is_feature_enabled("enable_simplepush")
    
    print(pushNotifications_is_enabled)
    print(simplePush_isEnabled)

    if pushNotifications_is_enabled:
        if simplePush_isEnabled:
            data = parse.urlencode({
            'key': PUSH_KEY, 'title': 'Train Alert!', 'msg': matchedText, 'event': 'Dart Issue'}).encode()     
            req = request.Request(PUSH_URL, data=data)     
            request.urlopen(req)

        else:       
            payload = {
            "app_key": PUSH_APP_KEY,
            "app_secret": PUSH_APP_SECRET,
            "target_type": "app",
            "content": matchedText
            }

            r = requests.post("https://api.pushed.co/1/push", data=payload)