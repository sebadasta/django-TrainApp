from apscheduler.schedulers.background  import BackgroundScheduler
from trainapp.functions import *

sched = BackgroundScheduler(timezone="Europe/Dublin")

PING_PROD_URL = os.environ.get('PING_PROD_URL')

@sched.scheduled_job('interval', minutes=1)
def timed_job():
  send_PushNotification("1 min job test")
  print('This job is run every one minute.')
  
@sched.scheduled_job('interval', minutes=10)
def check_ping():
  response = requests.get(PING_PROD_URL)
  print(response.status_code)



@sched.scheduled_job('cron',id="job_1", day_of_week='mon-sun', hour='8-23', minute='0/10')
def scheduled_job():
  checkDartIssues()
  print('This job is run on 0/10 8-23 * * 1-7')



def startScheduler():  
  if sched.state != 1:
    print("Starting Sched jobs")
    sched.start()
  
