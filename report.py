# -*- coding: utf-8 -*-

from tinydb import TinyDB, Query
from pprint import pprint

from petl import lookall
import sys
import yaml
import collections


from jinja2 import Template, Environment,PackageLoader,select_autoescape
db = TinyDB('db.json')

Q=Query()
report2 = [['Role','Tue','Wed','Thu','Fri','Sat','Sun']]


env = Environment(
    loader=PackageLoader('report', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),

)
env.trim_blocks=True
env.lstrip_blocks = True
template = env.get_template('report.html')


report = collections.OrderedDict();

# report['First Name'] = s['user']['firstname']
# shift['Last Name'] = s['user']['lastname']
# shift['Role'] =  s['role']['name'] if s['role']['name']  else "Please assign role"
# shift['Date'] =  s['shift']['start'].split(" ")[0]
# shift['Start'] =  s['shift']['start'].split(" ")[1].split(":")[0]
# shift['End'] = s['shift']['end'].split(" ")[1]

with open('roles.yaml', 'r') as f:
    doc = yaml.load(f)


am_kitchen = db.search(Q.shift.start.search('2017-12-15 0') & (Q.department.name=='Kitchen'))
pm_kitchen = db.search(Q.shift.start.search('2017-12-15 1') & (Q.department.name=='Kitchen'))

        #shifts = [str(r['shift']['start'][10:16] + " " + r['user']['firstname'] +  " " + r['user']['lastname']) for r in result]
        # shifts2 = zip(shifts[0::2], shifts[1::2])
        # pprint(list(shifts2))
        # report.append([role])
        # report.append([l for l in list(shifts2)])
        #report.append(list(shifts2))


#
#pprint(pm_kitchen)
print(template.render(am_kitchen=am_kitchen, pm_kitchen=pm_kitchen))


# result = db.search(Q.shift.start.search('14:00:00') & (Q.department.name=='Kitchen') & (Q.role.name=='Cold Buffeteer'))
# report.append(['Cold Buffeteer PM']+[r['shift']['start'] + ['user']['firstname'] + " " + r['user']['lastname'] for r in result])

#
# result = db.search( (Q.department.name=='Kitchen') \
#                     & (Q.role.name=='Cold Buffeteer')) \
#                     & (Q.shift.start.matches('*14:00:00*'))
#
# print (report)
# print(lookall(report))
