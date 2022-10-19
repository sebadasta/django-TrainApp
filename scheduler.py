from apscheduler.schedulers.background  import BackgroundScheduler
from trainapp.functions import *

sched = BackgroundScheduler(timezone="Europe/Dublin")
PUSH_APP_KEY = os.environ.get("PUSH_APP_KEY")
PUSH_APP_SECRET = os.environ.get("PUSH_APP_SECRET")

@sched.scheduled_job('interval', minutes=1)
def timed_job():
  print('This job is run every one minutes.')
  payload = {
  "app_key": PUSH_APP_KEY,
  "app_secret": PUSH_APP_SECRET,
  "target_type": "app",
  "content": "This is a test from Dart-App."
  }

  r = requests.post("https://api.pushed.co/1/push", data=payload)  
  

@sched.scheduled_job('interval', minutes=10)
def check_ping():
  response = requests.get("https://django-tranapp.onrender.com")
  print(response.status_code)



@sched.scheduled_job('cron',id="job_1", day_of_week='mon-sun', hour='8-23', minute='0/10')
def scheduled_job():
  checkDartIssues()
  print('This job is run on 0/10 8-23 * * 1-7')



def startScheduler():
    
  if sched.state != 1:
    sched.start()
  
