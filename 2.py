# 1 вариант

import requests

url = 'https://superheroapi.com/api/2619421814940190/'

result_dict = {}

resp_id_Hulk = requests.get(url+'/search/Hulk')
intelligance_Hulk = resp_id_Hulk.json()['results'][0]['powerstats']['intelligence']
result_dict['Hulk'] = intelligance_Hulk

resp_id_CapAm = requests.get(url+'/search/Captain America')
intelligance_CapAm = resp_id_CapAm.json()['results'][0]['powerstats']['intelligence']
result_dict['Captain America'] = intelligance_CapAm

resp_id_Thanos = requests.get(url+'/search/Thanos')
intelligance_Thanos = resp_id_Thanos.json()['results'][0]['powerstats']['intelligence']
result_dict['Thanos'] = intelligance_Thanos

print(result_dict)
max_intelligance = max(result_dict.items(), key=lambda x: x[0])
print(max_intelligance)

# 2 вариант

import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)

names_of_characters = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
intelligence = {}

for names in names_of_characters:
    response = requests.get(url)
    if response == 'success':
        intelligence[names] = intelligence.update(int(response['results'][0]['powerstats']['intelligence']))
print(intelligence)
