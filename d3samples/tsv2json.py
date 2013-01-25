__author__ = 'john.eo'

import csv
import random

with open("data.tsv") as tsv:
    with open("data.json", "w") as jdata:
        jdata.write("[")
        for line in csv.reader(tsv, dialect='excel-tab'):
            jdata.write('{ "date": "' + line[0]
                        + '","detractor": ' + str(random.randint(0, 100))
                        + ', "passive": ' + str(random.randint(0, 100))
                        + ', "promoter": ' + str(random.randint(0, 100))
                        + ' }, ')
        jdata.write("]")