#!/usr/local/bin/python3

import random

num = random.randint(1,199)

#num = 7

def plusOne(number=4, other="test"):
    num = number + 1
    return num

new_num = plusOne(other="one",number=num)

print(new_num)

#print("\n" + str(num) + " plusOne = " + str(plusOne(num)))
