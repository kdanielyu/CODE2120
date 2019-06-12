from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from bs4 import BeautifulSoup
import requests
from .models import *

# Create your views here.

def get(request, city):
    hostname = "https://en.wikipedia.org/wiki/"+str(city)
    req = requests.get(hostname)
    soup = BeautifulSoup(req.content, "html.parser")
    
    wikiLat = soup.find(class_='latitude')
    wikiLong = soup.find(class_='longitude')
    
    latInput = wikiLat.get_text()
    longInput = wikiLong.get_text()
    
    longOG = longInput
    longA = longOG.split("°")[0].split('′')
    longB = longOG.split("°")[1].split("′")[0]
    longC = longOG.split("′")[1].split("″")[0]
    longA = float(longA[0])/1
    longB = float(longB[0])/60
    if longC.isdigit():
        longC = float(longC[0])/3600
    else:
        longC = 0
        
    latOG = latInput
    latA = latOG.split("°")[0].split('′')
    latB = latOG.split("°")[1].split("′")[0]
    latC = latOG.split("′")[1].split("″")[0]
    latA = float(latA[0])/1
    latB = float(latB[0])/60
    try:
        latC = float(latC[0])/3600
    except ValueError:
        latC = 0

    lon = longA+longB+longC
    lat = latA+latB+latC
   
    return HttpResponse("lat: "+str(lat)+", lon: "+str(lon))

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