#!/usr/local/bin/python3

# Chapter 15 – Super Stopwatch

# ATBS-15_stopwatch.py 

import time

# display the program's instructions
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. \
Press Ctrl-C to quit")

# press ENTER to begin
input()
print("Started")

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap {lapNum}: {totalTime} {lapTime}")
        lapNum += 1
        lastTime = time.time()
        
except KeyboardInterrupt:
    print("\nDone.")
    pass