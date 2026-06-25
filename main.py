import requests

LAT = 48.669102
LNG = 12.690720

response = requests.get(url='https://api.sunrise-sunset.org/json')
response.raise_for_status()

data = response.json()

parameters = {
    'lat':LAT,
    'lng':LNG
}

