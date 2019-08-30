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
