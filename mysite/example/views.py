from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from bs4 import BeautifulSoup
import requests
from .models import *

# Create your views here.

def get(request, city):
	try:
		hostname = "https://www.google.com/maps/place/"+city
    	req = requests.get(hostname)
    	soup = BeautifulSoup(req.content, "html.parser")
    	return(soup)

def example_get(request, var_a):
	try:
		returnob = {
		"lon": "%s" %(var_a),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			return JsonResponse({"log":log})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")