#!/usr/bin/python3

'''
Unix time is the number of seconds elapsed since Unix epoch. 
The Unix epoch is the time 00:00:00 UTC on 1 January 1970 (or 1970- 01-01T00:00:00Z ISO 8601). 
The date and time in a computer is determined according to the number of seconds or clock ticks 
that have elapsed since the defined epoch for that computer or platform. 
'''

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch() 
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))