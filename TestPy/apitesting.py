'''
Created on 26 Mar 2015

@author: yvonne
'''

import json
import requests
from pprint import pprint


url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=b67945116c0e179d74fa5988aadc6090&format=json'
response = requests.get(url)
data = json.loads(response.text,encoding='utf-8')
artists = data['topartists']['artist']


pprint (artists[0]['name'])
#name = artists['artist']
#namess = artists ['name']



