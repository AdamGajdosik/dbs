
#!/usr/bin/python3

import json
import sys
from main import *

import os

test = Application()

listToSend = []
duplicates = []

baseId = test.getRaceId()+1
baseTrackId = test.getTrackId()
temp = 1

for root, dirs, files in os.walk('test'):

     for file in files:
        with open(os.path.join(root, file), "r") as f:
            zoznam = []
            #if (file[1] != '.'):
            #    continue
            try:
                print("!!!!!!!!!!!!!!SUBOR!!!!!!!!!!!!!!!!!!!" + root)
                for line in f.readlines():
                    zoznam.append(json.loads(line))
            except:
                continue

            a = 0
            data = []
            for i in zoznam:
                b = 0
                try:
                    oldBaseTrackId = baseTrackId
                    venue = zoznam[a]['mc'][0]['marketDefinition']['venue']
                    country = zoznam[a]['mc'][0]['marketDefinition']['countryCode']
                    timezone = zoznam[0]['mc'][0]['marketDefinition']['timezone']

                    if venue not in duplicates:
                        duplicates.append(venue)
                        baseTrackId+=1
                    command = ("INSERT INTO tracks(id,name,country,timezone) values(%d,'%s','%s','%s')"%(baseTrackId, venue,country,timezone))

                    if command not in listToSend:
                        listToSend.append(command)

                    eventId = zoznam[a]['mc'][0]['marketDefinition']['eventId']
                    eventTypeId = zoznam[a]['mc'][0]['marketDefinition']['eventTypeId']
                    numberOfWinners = zoznam[a]['mc'][0]['marketDefinition']['numberOfWinners']
                    eventName = zoznam[a]['mc'][0]['marketDefinition']['eventName']
                    time = zoznam[a]['mc'][0]['marketDefinition']['openDate']
                    status = zoznam[a]['mc'][0]['marketDefinition']['status']
                    command = ("INSERT INTO races(id, eventId, eventTypeId, eventName, numberOfWinners, time, status, track_id) values(%d,%d,%d,'%s',%d,'%s','%s', %d)"%(baseId, int(eventId), int(eventTypeId), eventName, numberOfWinners, time, status, baseTrackId))
                    oldBaseId = baseId
                    listToSend.append(command)
                    baseId+=1
                except:
                    a+=1
                    continue
                try:
                    for j in zoznam[a]['mc'][0]['marketDefinition']['runners']:
                        #print(b)
                        #print(zoznam[a]['mc'][0]['marketDefinition']['runners'][b])
                        name = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['name']
                        sortPriority = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['sortPriority']
                        adjustementFactor = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['adjustmentFactor']
                        status = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['status']
                        id = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['id']
                        command = ("INSERT INTO horses(id,name,sorting_priority,adjustement) values(%d,'%s',%d,%.2f)"%(id, name, sortPriority, adjustementFactor))
                        if name not in duplicates:
                            duplicates.append(name)
                            listToSend.append(command)
                        command = ("INSERT INTO race_horses(race_id, horse_id, status) values(%d,%d,'%s')"%(oldBaseId, id, status))
                        listToSend.append(command)
                        #venue = zoznam[0]['mc'][0]['marketDefinition']['venue']
                        #country = zoznam[0]['mc'][0]['marketDefinition']['countryCode']
                        #timezone = zoznam[0]['mc'][0]['marketDefinition']['timezone']
                        #test.dataImport(id,name, sortPriority, status, venue, country, timezone)
                        b+=1
                except:
                    print("nesu kone")
                    a+=1
                    continue
 
                #command = ("INSERT INTO horses(id,name,sorting_priority,status) values(%d,'%s',%d,'%s')"%(id, name, sortPriority, status))
                #command = ("INSERT INTO tracks(name,country,timezone) values('%s','%s','%s')"%(venue,country,timezone))
                #if command not in listToSend:
                #    listToSend.append(command)
                #print(data)
                #test.dataImport(0,"", 0, "", venue, country, timezone)
                a+=1
            #print(listToSend)
            #test.newImport(listToSend)
            
print(listToSend)
test.newImport(listToSend)

#test.dataImport(0,"", 0, "", venue, country, timezone)

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

