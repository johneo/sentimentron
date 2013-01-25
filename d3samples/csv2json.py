__author__ = 'john.eo'

import csv
import random

with open("data.csv") as cdata:
    with open("data.json", "w") as jdata:
        jdata.write("[")
        for line in csv.reader(cdata):
            jdata.write('{ "key": "' + line[0]
                        + '","value": ' + line[1]
                        + ', "date": "' + line[2]
                        + '" }, ')
        jdata.write("]")