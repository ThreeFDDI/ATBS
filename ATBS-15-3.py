#!/usr/local/bin/python3

# Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

# ATBS-15-3.py 

import time, datetime

startTime = datetime.datetime(2029, 10, 31)
while datetime.datetime.now() < startTime:
    print("SLEEP")
    time.sleep(10)