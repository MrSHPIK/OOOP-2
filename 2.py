import json
from pprint import pprint
import requests

def super_heroes():
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url=url)
return response

intelligence_super_man = 0
name = ''
for intelligence_super in super_hero:
    if intelligence_super_man < int(intelligence_super['intelligence']):
        intelligence_super_man = int(intelligence_super['intelligence'])
        name = intelligence_super['name']

print(f"Самый умный {name}, интелект: {intelligence_super_man}")
heroes()