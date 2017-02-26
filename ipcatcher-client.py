#!/usr/bin/python3
import requests
import os
from datetime import datetime

key = os.environ['IPCATCHER_KEY']

r = requests.post('http://ipcatcher.tjsimmons.net/services/', data={'key': key})

print(datetime.now())
print(r.text)
print(r.status_code)
print('\n')
