from apscheduler.schedulers.blocking import BlockingScheduler
from trainapp.functions import *

sched = BlockingScheduler(timezone="Europe/Dublin")

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
 #   print('This job is run every one minutes.')

@sched.scheduled_job('cron',id="job_1", day_of_week='mon-fri', hour='8-23', minute='0,29')
def scheduled_job():
  checkDartIssues()
  print('This job is run on 0,29 8-23 * * 1-5')


#sched.start()
def startScheduler():
    
  if sched.state != 1:
    sched.start()

