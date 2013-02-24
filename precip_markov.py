#!/usr/bin/env python
#
# Inspired by the code from 
# http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
#
# This code, however, does doubles or triples and uses numpy to create a transformation matrix.
#
# Expects the first command line argument to be a file that has precipitation amounts.

import numpy as np
from sys import argv

class Markov():
    def __init__(self,data,order = 3):
        self.data = data
        self.transform = {}
        if order == 3:
            self.build_transform()
        elif order == 2:
            self.build_transform_doubles()

    def triples(self):
        if len(self.data) < 3:
            return
        
        for i in range(len(self.data) - 2):
            yield (self.data[i], self.data[i+1], self.data[i+2])

    def doubles(self):
        if len(self.data) < 2:
            return
        
        for i in range(len(self.data) - 1):
            yield (self.data[i], self.data[i+1])

    def build_transform(self):
        retval = []
        for (v1,v2,v3) in self.triples():
            key = (v1,v2)
            if key not in self.transform:
                self.transform[key] = [v3]
            else:
                self.transform[key].append(v3)
        return retval

    def build_transform_doubles(self):
        retval = []
        for (v1,v2) in self.doubles():
            key = v1
            if key not in self.transform:
                self.transform[key] = [v2]
            else:
                self.transform[key].append(v2)
        return retval

            
data = np.loadtxt(argv[1])
m = Markov(data != 0,2)
print("|rain, clear>")
list = []
for state in m.transform:
    transitions = np.array(m.transform[state])
    print(state)
    count = float(len(transitions))
    rain = len(transitions[transitions == True])/count
    clear = 1 - rain
    print("(%f,%f)" % (rain,clear))
    list.append((rain,clear))

transform = np.array(list)

print()
transform.reshape(-1,2)
state = np.array([1,0])
print("%s * %s" % (state,transform))
print(np.dot(state,transform))

print()
state = np.array([0,1])
print("%s * %s" % (state,transform))
print(np.dot(state,transform))






