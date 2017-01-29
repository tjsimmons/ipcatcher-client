#!/usr/bin/python
import requests
import os

key = os.environ['IPCATCHER_KEY']

r = requests.post('http://ipcatcher.tjsimmons.net/services/', data={'key': key})

print(r.text)
print(r.status_code)
