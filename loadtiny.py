from tinydb import TinyDB, Query
import requests
from pprint import pprint
db = TinyDB('db.json')

for offset in range(0, 500, 50):
    limit=50
    print(offset)
    u = 'https://api.7shifts.com/v1/shifts?start[gte]=2017-12-12 00:00:00&start[lte]=2017-12-17 23:59:59&deep=1&limit=50&offset={0}'.format(offset)
    print(u)
    r = requests.get(u, auth=('86SM3M44RYM7JTBHQB3J6NDM4GKKA3SZ', ''))
    print(r.status_code)
    payload_length =  len(r.json()['data'])
    print("Payload", payload_length)
    if payload_length == 0: break
    for s in r.json()['data']:
        db.insert(s)
