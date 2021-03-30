from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import *
import requests, zipfile, io,csv,pickle
from datetime import date,datetime,timedelta
import time
from django.conf import settings


sched = BackgroundScheduler({
	"apscheduler.jobstores.default": {
		"class": "django_apscheduler.jobstores:DjangoJobStore"
	},
	'apscheduler.executors.default': {
		'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
		'max_workers': '20'
	},
	'apscheduler.executors.processpool': {
		'type': 'processpool',
		'max_workers': '8'
	},
	'apscheduler.job_defaults.coalesce': 'false',
	'apscheduler.job_defaults.max_instances': '5',
	'apscheduler.timezone': 'UTC',
})


def download_data():
	""" this is the function used for downloadinf zip file from BhavCopy site"""
	try:
		filename = 'EQ'+date.today().strftime('%d%m%y')+'_CSV.ZIP'
		ext_filename = 'EQ'+date.today().strftime('%d%m%y')+'.CSV'
		url = 'https://www.bseindia.com/download/BhavCopy/Equity/'+filename
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		r = requests.get(url, headers=headers)
		z = zipfile.ZipFile(io.BytesIO(r.content))
		data = pickle.loads(settings.R_SERVER.get("zerodha_data") or pickle.dumps({}))
		z.extractall('/usr/local/src/zerodha')
		reader = csv.DictReader(open('/usr/local/src/zerodha/EQ250321.CSV', 'r'))
		data = [dict(line) for line in reader]
		settings.R_SERVER.set("zerodha_data", pickle.dumps(data))
	except Exception as e:
		print(e)
		pass

def start_daemon():

	""" this is the function used for runing deamon service continuesly"""
	
	download_data_time = datetime.strptime('00:00','%H:%M') - timedelta(hours=11, minutes=00)
	sched.add_job(download_data, 'cron', day_of_week='*', hour=download_data_time.hour, minute=download_data_time.minute, replace_existing=True,id='download_data')
	if sched.state == 0:
		sched.start()
	while True:
		time.sleep(30)
		print("hello dinesh")
