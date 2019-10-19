from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


class WeatherViewSet(APIView):

    def post(self, request, **kwargs):
        if request.method != "POST":
            return HttpResponse("POST request only")
              
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city = kwargs["location"]
        city_weather = requests.get(url.format(city)).json()
        print(city_weather)
        return JsonResponse(city_weather)


