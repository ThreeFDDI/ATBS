#!/usr/local/bin/python3

def collatz(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    print(num)
    return num


num = input("Please pick a number to run the Collatz swquence against:\n")

#print(num)

try:
    num = int(num)

    while num != 1:
        num = collatz(num)

except ValueError:
    print("You did not enter a number.\n")


