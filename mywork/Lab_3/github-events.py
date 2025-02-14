#!/usr/bin/python3
import os
import json
import requests

GHUSER = os.getenv('sofia-cojocea')
url = 'https://api.github.com/users/{0}/events'.format(GHUSER)

r = json.loads(requests.get(url).text)

for x in r[:5]:
	event = x['type'] + ' :: ' + x['repo']['name']
	print(event)

print(r)
