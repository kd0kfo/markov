#!/usr/bin/env python

import numpy as np
import json
from sys import argv

fn = argv[1]

json_file = open(fn,"r")
json_data = json.loads(json_file.read())
json_file.close()

observations = json_data['history']['observations']
temps = []
precips = []
for obs in observations:
    #print("%s:%s  %s %s" % (obs['date']['hour'],obs['date']['min'],obs['tempi'],obs['precipi']))
    temps.append(float(obs['tempi']))
    if obs['precipi'] != "T":
        precip = float(obs['precipi'])
        if precip > 0:
            precips.append(precip)

print("Average temperature is %0.1fF" % np.mean(temps))
if precips:
    print("Average precipitation is %0.2f inches" % np.mean(precips))
    print("Total precipitation is %0.2f inches" % np.sum(precips))
daily_precip = json_data['history']['dailysummary'][0]['precipi']
if daily_precip == "T":
    daily_precip = 0
print("Daily precipitation value %s" % daily_precip)
