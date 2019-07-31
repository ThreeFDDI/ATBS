#!/usr/local/bin/python3

import random
import sys

def guess(secret_number, guesses):
    print("You have {} tries left to guess the number...".format(7 - guesses))
    guesses += 1
    guess = int(input("What's your guess? "))

    if guess == secret_number:
        print("\nCongratulations, you've guessed correctly!!\n")
        sys.exit()

    elif guess < secret_number:
        print("Your guess ({}) was too low.".format(guess))
        
    elif guess > secret_number:
        print("Your guess ({}) was too high.".format(guess))
    
    return guesses

secret_number = random.randint(1,20)

guesses = 1

print("\n*** Secret number is: {} ***\n".format(secret_number))
print("I am thinking of a number between 1 and 20.")

while guesses <= 6:
    guesses = guess(secret_number,guesses)

print("\nSorry, you've run out of guesses.\n")
