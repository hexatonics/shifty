from tinydb import TinyDB, Query
import petl as etl
from pprint import pprint
db = TinyDB('db.json')
Q=Query()
import sys

import collections

#find shifts for today for a role and make a
fi =  open("rep.txt", "w")
fi.write("\n\n\n\t\t\t\t  Schedule \n")
fi.write("\t\t\t\t------------\n\n")
fi.write("\tTUE\t\tWED\t\tTHUR\t\tFRI\t\t\tSAT\t\tSUN")
