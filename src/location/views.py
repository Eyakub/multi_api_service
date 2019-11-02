from django.shortcuts import render
import requests
from app.credientials import *


def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        response = requests.get(
            'http://api.ipstack.com/' + IP_ADDRESS + '?access_key=' + ACCESS_KEY + '&format=1')
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': API_KEY,
        'is_cached': is_cached,
    }
    return render(request, 'home.html', context)
