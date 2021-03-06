#!/usr/bin/python3

class TimeParser:

    @staticmethod
    def toDate(info):
        info = str(info)
        date = ""
        date += str(info[0:2]) + "." + str(info[2:4]) + "." + str(info[4:6])
        return date

    @staticmethod
    def toTime(info):
        info = str(info)
        time = ""
        time += str(info[0:2]) + ":" + str(info[2:4]) + ":" + str(info[4:6])
        return time