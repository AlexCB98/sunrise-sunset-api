import requests


# https://www.latlong.net/
LAT = 48.669102
LONG = 12.690720

parameters = {
    'lat':LAT,
    'lng':LONG,
    'formatted':0
}

response = requests.get(
    url='https://api.sunrise-sunset.org/json',
    params=parameters,
)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset  = data['results']['sunset'].split('T')[1].split(':')[0]

print(f'The sunrise will be at: {sunrise}')
print(f'The sunset will be at: {sunset}')
