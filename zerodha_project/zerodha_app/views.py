from django.shortcuts import render
from django.conf import settings
import redis,pickle


def DataList(request):

	""" this function is used for redering the download data into front end """

	data = pickle.loads(settings.R_SERVER.get("zerodha_data") or pickle.dumps({}))
   
	return render(request, "plot_data.html",{"data":data}) 