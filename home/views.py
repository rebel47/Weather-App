from django.http import response
from django.shortcuts import render
# from django.http import HttpResponse
import requests


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def index(request):
    area = request.GET.get('area')
    area = str(area)
    baserUrl = 'https://api.weatherapi.com/v1/current.json?key=e7a6fabfe4ae403280593925210208&q={}&aqi=yes'.format(area)
    response = requests.get(baserUrl).json()

    city_weather = {
        'City': response['location']['region'],
        'Time': response['location']['localtime'],
        'Celcius': response['current']['temp_c'],
        'Fahrenheit': response['current']['temp_f'],
        'Condition': response['current']['condition']['text'],
        'Icon': response['current']['condition']['icon'],
        'WindSpeed': response['current']['wind_mph'],
        'WindDirection': response['current']['wind_dir'],
        'Humidity': response['current']['humidity'],
    }
    # print(city_weather)
    # print(response.text)


    return render(request, 'index.html', {'city_weather': city_weather})