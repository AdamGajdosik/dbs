
#!/usr/bin/python3

import json
import sys
from main import *

import os

test = Application()

listToSend = []
duplicates = []

#baseId = test.getRaceId()+1
#baseTrackId = test.getTrackId()
temp = 1

for root, dirs, files in os.walk('alldata/2015/May'):

     for file in files:
        with open(os.path.join(root, file), "r") as f:
            baseId = test.getRaceId()+1
            baseTrackId = test.getTrackId()
            zoznam = []
            #if (file[1] != '.'):
            #    continue
            try:
                print("!!!!!!!!!!!!!!SUBOR!!!!!!!!!!!!!!!!!!!" + os.path.join(root, file))
                for line in f.readlines():
                    zoznam.append(json.loads(line))
            except:
                continue

            a = 0
            data = []
            for i in zoznam:
                b = 0
                try:
                    command = " "
                    oldBaseTrackId = baseTrackId
                    venue = zoznam[a]['mc'][0]['marketDefinition']['venue']
                    country = zoznam[a]['mc'][0]['marketDefinition']['countryCode']
                    timezone = zoznam[0]['mc'][0]['marketDefinition']['timezone']
                    isThere = test.testForSameTrack(venue)
                    if venue not in duplicates and isThere !=1:
                        duplicates.append(venue)
                        baseTrackId+=1

                    if isThere != 1:
                        command = ("INSERT INTO tracks(id,name,country,timezone) values(%d,'%s','%s','%s')"%(baseTrackId, venue,country,timezone))

                    if command not in listToSend and isThere !=1 and command != " ":
                        listToSend.append(command)

                    command = " "
                    eventId = zoznam[a]['mc'][0]['marketDefinition']['eventId']
                    eventTypeId = zoznam[a]['mc'][0]['marketDefinition']['eventTypeId']
                    numberOfWinners = zoznam[a]['mc'][0]['marketDefinition']['numberOfWinners']
                    eventName = zoznam[a]['mc'][0]['marketDefinition']['eventName']
                    time = zoznam[a]['mc'][0]['marketDefinition']['openDate']
                    status = zoznam[a]['mc'][0]['marketDefinition']['status']
                    if isThere == 1:
                        command = ("INSERT INTO races(id, eventId, eventTypeId, eventName, numberOfWinners, time, status, track_id) values(%d,%d,%d,'%s',%d,'%s','%s', %d)"%(baseId, int(eventId), int(eventTypeId), eventName, numberOfWinners, time, status, test.getSameTrackId(venue)[0][0]))
                    else:
                        command = ("INSERT INTO races(id, eventId, eventTypeId, eventName, numberOfWinners, time, status, track_id) values(%d,%d,%d,'%s',%d,'%s','%s', %d)"%(baseId, int(eventId), int(eventTypeId), eventName, numberOfWinners, time, status, baseTrackId))
                    if command!= " ":
                        oldBaseId = baseId
                        listToSend.append(command)
                        baseId+=1
                except:
                    #print("padne 1")
                    a+=1
                    continue
                try:
                    for j in zoznam[a]['mc'][0]['marketDefinition']['runners']:
                        command = " "
                        name = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['name']
                        sortPriority = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['sortPriority']
                        adjustementFactor = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['adjustmentFactor']
                        status = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['status']
                        id = zoznam[a]['mc'][0]['marketDefinition']['runners'][b]['id']
                        if test.testForSameHorse(name) != 1:
                            command = ("INSERT INTO horses(id,name,sorting_priority,adjustement) values(%d,'%s',%d,%.2f)"%(id, name, sortPriority, adjustementFactor))
                        if name not in duplicates and command != " ":
                            duplicates.append(name)
                            listToSend.append(command)
                        command = " "
                        command = ("INSERT INTO race_horses(race_id, horse_id, status) values(%d,%d,'%s')"%(oldBaseId, id, status))
                        if command!= " ":
                            listToSend.append(command)
                        b+=1
                except:
                    #print("nesu kone")
                    #print("padne 2")
                    a+=1
                    continue
                a+=1
        print(listToSend)
        test.newImport(listToSend)
        listToSend = []
            #print(listToSend)
            #test.newImport(listToSend)
            
#print(listToSend)
#test.newImport(listToSend)

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

