#!/usr/bin/python3

import json
import sys
from main import *


import os

test = Application()

for root, dirs, files in os.walk('mydata'):

     for file in files:
        with open(os.path.join(root, file), "r") as f:
            zoznam = []
            #if (file[1] == '.'):
            #    continue
            try:
                print("!!!!!!!!!!!!!!SUBOR!!!!!!!!!!!!!!!!!!!" + root)
                for line in f.readlines():
                    zoznam.append(json.loads(line))
            except:
                continue

            a = 0
            for i in zoznam:
                b = 0
                try:
                    for j in zoznam[a]['mc'][0]['marketDefinition']['runners']:
                        #print(b)
                        #print(zoznam[a]['mc'][0]['marketDefinition']['runners'][b])
                        #name = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['name']
                        #sortPriority = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['sortPriority']
                        #adjustementFactor = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['adjustmentFactor']
                        #status = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['status']
                        #id = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['id']

                        #venue = zoznam[0]['mc'][0]['marketDefinition']['venue']
                        #country = zoznam[0]['mc'][0]['marketDefinition']['countryCode']
                        #timezone = zoznam[0]['mc'][0]['marketDefinition']['timezone']
                        #test.dataImport(id,name, sortPriority, status, venue, country, timezone)
                        b+=1
                except:
                    #print("picovina")
                    a+=1
                    continue
                try:
                    venue = zoznam[a]['mc'][0]['marketDefinition']['venue']
                    country = zoznam[a]['mc'][0]['marketDefinition']['countryCode']
                    timezone = zoznam[0]['mc'][0]['marketDefinition']['timezone']
                except:
                    continue
                test.dataImport(0,"", 0, "", venue, country, timezone)
                a+=1


#with open("data", 'r') as f:
#    zoznam = []
#    for line in f.readlines():
#        zoznam.append(json.loads(line))

##print(zoznam[0]['op']);
##print(zoznam[0]['clk']);
##print(zoznam[0]['mc'][0]);
##print(zoznam[0]['mc'][0]['marketDefinition']['eventId']);
##print(zoznam[0]['mc'][0]['marketDefinition']['eventTypeId']);
##print(zoznam[0]['mc'][0]['marketDefinition']['numberOfWinners']);
##print(zoznam[0]['mc'][0]['marketDefinition']['eventName']);
##print(zoznam[0]['mc'][0]['marketDefinition']['complete']);
##print(zoznam[0]['mc'][0]['marketDefinition']['runners']);

#print(zoznam[0]['mc'][0]['marketDefinition']['venue']);
#print(zoznam[0]['mc'][0]['marketDefinition']['countryCode']);
#print(zoznam[0]['mc'][0]['marketDefinition']['timezone']);
##races:
#id() | eventTypeId() | eventName() | numberOfWinners() | complete() | runners()

#test = Application()
#test.dataImport("adam")

#a=0
#b = 0
#print(zoznam[a]['mc'][0]['marketDefinition']['runners'][b])
#name = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['name']
#sortPriority = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['sortPriority']
#adjustementFactor = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['adjustmentFactor']
#status = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['status']
#id = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['id']
#test.dataImport(id,name, sortPriority, status)

