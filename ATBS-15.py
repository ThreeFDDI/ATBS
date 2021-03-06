#!/usr/local/bin/python3

# Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs

# ATBS-15.py 

import time

#print(time.time())

def calcProd():
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 1000000):
           product = product * i
       return product

startTime = round(time.time())
prod = calcProd()
endTime = round(time.time())
#print(prod)
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

for i in range(5):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)

