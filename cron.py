#cron jobs
#sudo pip install apscheduler
# see https://impythonist.wordpress.com/2014/11/13/how-to-wake-up-a-python-script-while-you-are-in-a-sound-sleep/
#1 db racesps.py
#2 update db
#3 compute cols
#3 stats
# from apscheduler.scheduler import Scheduler
from apscheduler.schedulers.background import BackgroundScheduler
#start the scheduler i.e create instance

sched=BackgroundScheduler()




@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
def my_job():
    print 'Happy_Birthday,Aryan'
#schedules job function my_job to greet me every year on my Birthday

sched.start()

sched.print_jobs()