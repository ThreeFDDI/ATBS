#!/usr/local/bin/python3

# Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

# ATBS-15-3.py 

import time, datetime, threading

startTime = datetime.datetime(2029, 10, 31)
#while datetime.datetime.now() < startTime:
#    print("\nNOT YET!!")
#    time.sleep(10)

def takeANap():
    print("Sleep...")
    time.sleep(5)
    print("Wake up!!")

threadObj = threading.Thread(target=takeANap)

threadObj.start()


print(type(threadObj))
