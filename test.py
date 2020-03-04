#!/usr/bin/python3

import json

with open("data", 'r') as f:
    zoznam = []
    for line in f.readlines():
        zoznam.append(json.loads(line))

print(zoznam[0]['op']);
print(zoznam[0]['clk']);
#print(zoznam[0]['mc'][0]);
print(zoznam[0]['mc'][0]['marketDefinition']['runners']);


"""
for i in zoznam:
    a = 0
    print(zoznam[a]['clk']);
    a+=1
"""