import requests
import json
data = {
    'type' : 'motorcycle',
    'origin' : ',',
    'destination' : ','
}
data = json.dumps(data)
response = requests.get(
    url=' https://api.neshan.org/v1/distance-matrix/no-traffic?type=car&origins=35.841099,50.967880&destinations=48.51925179,34.77754899',
    data = data,
    headers={'Api-Key':'service.b3fa53fc30254c16ac0dc094deea13e4'}
)
print(response.text)
print(response)
print()

