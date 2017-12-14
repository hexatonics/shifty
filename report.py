from tinydb import TinyDB, Query
import requests
from pprint import pprint
db = TinyDB('db.json')
from petl import lookall
import sys
import yaml

Q=Query()
report = [['Role','Tue','Wed','Thu','Fri','Sat','Sun']]

with open('roles.yaml', 'r') as f:
    doc = yaml.load(f)

for key in doc.keys():



    print("\t DEPARTMENT ", key)

    roles = doc[key].values()
    for role in roles:
        print("\t ROLE ", role)

        # You want a column that is 
        result = db.search((Q.shift.start.search('2017-12-15') & Q.department.name==key) & (Q.role.name==role))
        shifts = [str(r['shift']['start'][10:16] + " " + r['user']['firstname'] +  " " + r['user']['lastname']) for r in result]
        print(shifts)
        # shifts2 = zip(shifts[0::2], shifts[1::2])
        # pprint(list(shifts2))
        # report.append([role])
        # report.append([l for l in list(shifts2)])
        #report.append(list(shifts2))








# result = db.search(Q.shift.start.search('14:00:00') & (Q.department.name=='Kitchen') & (Q.role.name=='Cold Buffeteer'))
# report.append(['Cold Buffeteer PM']+[r['shift']['start'] + ['user']['firstname'] + " " + r['user']['lastname'] for r in result])

#
# result = db.search( (Q.department.name=='Kitchen') \
#                     & (Q.role.name=='Cold Buffeteer')) \
#                     & (Q.shift.start.matches('*14:00:00*'))
#
# print (report)
print(lookall(report))
