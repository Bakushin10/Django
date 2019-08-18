from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def get_weather_API(request):

    if request.method != "GET":
        return HttpResponse("GET request only")
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = "gainesville"
    city_weather = requests.get(url.format(city)).json()
    return JsonResponse(city_weather)
    

