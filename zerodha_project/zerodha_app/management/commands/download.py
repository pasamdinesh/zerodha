from django.core.management.base import BaseCommand
from optparse import make_option
import time
import logging
class Command(BaseCommand):

	help = "Describe AutoDial Commands"
	def handle(self, **options):
		logging.basicConfig(format='[%(asctime)s] %(levelno)s' \
				'(%(process)d) %(module)s: %(message)s', level=logging.DEBUG)
		logging.debug("Starting AutoDial Daemon...")
		logging.warning("download Daemon is running...")
		logging.warning("Quit the daemon with CONTROL-C")
		from zerodha_app import utility
		utility.start_daemon()
		# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
		# # result = requests.get(url, headers=headers)
		# r = requests.get(url, headers=headers)
		# z = zipfile.ZipFile(io.BytesIO(r.content))
		# data = pickle.loads(settings.R_SERVER.get("zerodha_data") or pickle.dumps({}))
		# z.extractall('/usr/local/src/zerodha')
		# # data = csv.DictReader(open('/usr/local/src/zerodha/'+ext_filename, 'r'))
		# reader = csv.DictReader(open('/usr/local/src/zerodha/EQ190321.CSV', 'r'))
		# data = [dict(line) for line in reader]
		# settings.R_SERVER.set("zerodha_data", pickle.dumps(data))
