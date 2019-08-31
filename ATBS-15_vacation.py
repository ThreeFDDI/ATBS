#!/usr/local/bin/python3

# Chapter 15 – Vacation countdown

# ATBS-15_vacation.py 

import datetime, time

# set current time
dt = datetime.datetime.now()

# set vacation date
vacation = datetime.datetime(2019, 11, 2)

# calculate delta between them
delta = vacation -  dt

# print vacation countdown
print(f"\nOnly {delta.days} days until vacation!!")