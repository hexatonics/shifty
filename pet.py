from tinydb import TinyDB, Query
import petl as etl
from pprint import pprint
db = TinyDB('db.json')
Q=Query()
import sys

import collections


#find shifts for today for a role and make a
#fi =  open("report.txt", "w")
#report=[['Role','2017-12-12','2017-12-13','2017-12-14','2017-12-15','2017-12-16','2017-12-17']]


def mini(s):
    shift = collections.OrderedDict();
    shift["Day"]=s['shift']['start'][0:10]
    shift["Department"]=s['department']['name']
    # shift["Role"]=s['role']['name'][0:9] + " " + s['shift']['start'][11:16].lstrip("0")
    # shift["Name"]=s['user']['firstname'] + " " + s['user']['lastname'][0:1]
    shift["Shift"]=s['role']['name'][0:9] + " " + s['shift']['start'][11:16].lstrip("0") + " " + s['user']['firstname'] + " " + s['user']['lastname'][0:1]

    return shift

def compact(s):
    shift = s['role']['name'][0:14] + " " + s['shift']['start'][11:16].lstrip("0") + " " + s['user']['firstname'] + " " + s['user']['lastname'][0:1]
    #shift["Notes"]=s['shift']['notes']
    return shift


data = [mini(s) for s in db]
pprint(data)
table = etl.fromdicts(data)

pprint(etl.look(table))


#Using set get a list of distinct departments

departments = (set(etl.values(table,"Department")))
pprint(departments)

for d in departments:
    print(d)
    table2 = etl.select(table, 'Department', lambda v: v == d ).facet("Day" )
    report = (
          etl
         .empty()
         .addcolumn('12-13', list(table2["2017-12-13"].values("Shift")))
         .addcolumn('12-14', list(table2["2017-12-14"].values("Shift")))
         .addcolumn('12-15', list(table2["2017-12-15"].values("Shift")))
         .addcolumn('12-16', list(table2["2017-12-16"].values("Shift")))
         .addcolumn('12-17', list(table2["2017-12-17"].values("Shift")))

         )


    pprint(etl.lookall(report,style='minimal'))
# sys.exit()

#
# table15 = table['2017-12-15']
# print(etl.look(table15))
# table16 = table['2017-12-16']
# table17 = table['2017-12-17']
# full = etl.annex(table15, table16,table17)
# print(etl.lookall(full))
 # etl.addcolumn(table1, 'baz', col)
 #table2 = etl.addfield(table1, 'baz', 42)
#etl.addfieldusingcontext(table1, 'baz', upstream)
#etl.addfieldusingcontext(table2, 'quux', downstream)

 #
 # etl.annex(table1, table2)
#table2, table3 = etl.biselect(table, lambda rec: rec.foo == 'a')
# day2 = call_day('2017-12-16')
# day3 = call_day('2017-12-17')


#foo1 = etl.facet(day1)


sys.exit()
table = (
     etl
    .empty()
     .addcolumn('15', day1)
     .addcolumn('16', day2)
     .addcolumn('17', day3)
 )

print(etl.look(table))



etl.tocsv(table, 'table.csv')


#
# roles=['Cook', 'Cheerleader', 'Assistant Cook']
# table2 = addcolumn(report, 'Role', roles)
# #
#
# table=[
# ['dept','role','start','name','DAY'],
# ['Kitchen','Cook','06:00','Jenny','12'],
# ['Kitchen','Diswasher','06:00','Tom','12'],
# ['Kitchen','Cook','06:00','Jenny','13'],
# ['Kitchen','Diswasher','06:00','Wil','13'],
# ['Bakery','Baker','06:00','Rebecca','12'],
# ['Bakery','Baker2','06:00','Stephanie','13']
#     ]
# print(look(table))
# table2=transpose(table)
# table3=aggregate(table, key=('DAY', 'dept'),aggregation=list, value=( 'role','start','name'))
# print(lookall(table3))
# table4=transpose(table3)
# print(lookall(table4))




#data = db.search(Q.role.name=='Cook')
# for i,d in enumerate(data):
#     fi.write(d['shift']['start'] + "\t")
# fi.write("\n")
