from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="Europe/Dublin")

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
 #   print('This job is run every one minutes.')

@sched.scheduled_job('cron',id="job_1", day_of_week='mon-fri', hour='8-23', minute='0/15')
def scheduled_job():
  print('This job is run on 0/15 8-23 * * 1-5')

sched.start()  
