# This package is useful for dealing with simple data stuff, like saving data to a csv file
import petl  as etl
from pprint import pprint
import json
import requests
import sys
import datetime
import collections
now = datetime.datetime.now()
today= now.strftime("%Y-%m-%d")
print("*******************************************")
print("         SCHEDULE for {0}                   ".format(today))
print("*******************************************")
# curl https://api.7shifts.com/v1/locations -u 86SM3M44RYM7JTBHQB3J6NDM4GKKA3SZ:

def foo(calltype,dataname):
    r = requests.get(   'https://api.7shifts.com/v1/{0}'.format(calltype), auth=('86SM3M44RYM7JTBHQB3J6NDM4GKKA3SZ', ''))
    print(r.status_code)
    j = r.json()['data']
    print(type(j))
    pprint(j)
    return [d[dataname] for d in j]


def shifts(day):

    '''
    Pass in day of the week, and get all the shifts for today
    '''
    # Get todays date based on the day of the week

    data = {}#'{ "punch_id": 1234 }'
    # get todays date
    u = 'https://api.7shifts.com/v1/shifts?start[gte]=2017-12-01 00:00:00&start[lte]=2017-12-10 23:59:59&deep=1?limit=50'
    r = requests.get(u, data=data, auth=('86SM3M44RYM7JTBHQB3J6NDM4GKKA3SZ', ''))
    print(r.status_code)
    j = r.json()['data']

    return j# [d['shift'] for d in j]

#shifts = foo('shifts', 'shift')
##

# pprint(current_shifts())
# pprint(len(current_shifts()))

with open('testdata.json') as json_data:
    d = json.load(json_data)

report = []
class Shift(object):
    ''' Shift view Object takes a raw shift dict from deep 7Shifts object, and turns it
    into a row that resembles
    '''
    def __init__(self):
        pass
    def name():
        pass
print("Current date using strftime:")
today= now.strftime("%Y-%m-%d")

def getit():
    for n,s in enumerate(shifts()):
        shift = collections.OrderedDict();
        shift['First Name'] = s['user']['firstname']
        shift['Last Name'] = s['user']['lastname']
        shift['Role'] =  s['role']['name'] if s['role']['name']  else "Please assign role"
        shift['Date'] =  s['shift']['start'].split(" ")[0]
        shift['Start'] =  s['shift']['start'].split(" ")[1].split(":")[0]
        shift['End'] = s['shift']['end'].split(" ")[1]

        pprint(shift)
        report.append(shift)

    t = etl.fromdicts(report)
    print(etl.lookall(t))

from datetime import datetime, timedelta

now =  datetime.now()
start = now - timedelta(days=now.weekday())
end = start + timedelta(days=6)
print(start)
print(end)

print(start.strftime('%d-%b-%Y'))
print(end.strftime('%d-%b-%Y'))



#
# for u in users:
#     uid  = (u['id'])
#     # find shifts for this user
#     user_shifts = [s['start'] for s in shifts if s['user_id'] == uid]
#     #print(user_shifts)
#     report.append((u['id'],"{0} {1}".format(u['firstname'],u['lastname']),user_shifts))
#
# pprint(report)
