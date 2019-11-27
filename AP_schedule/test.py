# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def aps_pause(x):
    scheduler.pause_job('interval_task')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def aps_resume(x):
    scheduler.resume_job('interval_task')
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5', id='cron_task')

scheduler.add_job(func=aps_pause, args=('一次性任务,停止循环任务',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12), id='pause_task')

scheduler.add_job(func=aps_resume, args=('一次性任务,恢复循环任务',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=24), id='resume_task')

scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3, id='interval_task')
scheduler._logger = logging

scheduler.start()
