__author__ = 'john.eo'

import csv

with open("data.tsv") as tsv:
    with open("data.json", "w") as jdata:
        jdata.write("[")
        for line in csv.reader(tsv, dialect='excel-tab'):
            jdata.write('{ "date": "' + line[0] + '", "value": ' + line[1] + ' }, ')
        jdata.write("]")