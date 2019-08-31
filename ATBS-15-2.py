#!/usr/local/bin/python3

# Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

# ATBS-15-2.py 

import datetime, time

print(datetime.datetime.now())
print()

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print()
print(dt.hour, dt.minute, dt.second)
print()

print(datetime.datetime.fromtimestamp(1000000))
print()

print(datetime.datetime.fromtimestamp(time.time()))
print()

delta =  datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(delta.days, delta.seconds, delta.microseconds)
print()
print(delta.total_seconds())
print()
print(type(delta))
print()
print(delta)
print()
print(str(delta))
print()

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

cruise = datetime.datetime(2019, 12, 2)

print(dt - cruise)