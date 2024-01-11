import requests
import json
data = {
    'type' : 'motorcycle',
    'origin' : ',',
    'destination' : ','
}
data = json.dumps(data)
response = requests.get(
    url='https://api.neshan.org/v4/direction?type=car&origin=34.77723862645681,48.52053860649812&destination=34.79368700172722,48.503407063998566&avoidTrafficZone=false&avoidOddEvenZone=false&alternative=false&bearing=',
    data = data,
    headers={'Api-Key':'service.b3fa53fc30254c16ac0dc094deea13e4'}
)
print(response.text)
print(response)
print()

