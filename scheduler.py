from apscheduler.schedulers.background  import BackgroundScheduler
from trainapp.functions import *

sched = BackgroundScheduler(timezone="Europe/Dublin")

@sched.scheduled_job('interval', minutes=1)
def timed_job():
  print('This job is run every one minutes.')

@sched.scheduled_job('cron',id="job_1", day_of_week='mon-sun', hour='8-23', minute='0/5')
def scheduled_job():
  #checkDartIssues()
  print('This job is run on 0/15 8-23 * * 1-7')



def startScheduler():
    
  if sched.state != 1:
    sched.start()
  
