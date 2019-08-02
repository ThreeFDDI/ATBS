#!/usr/local/bin/python3

import random

print("Hello", end=" ")
print("World,", end=" ")
print("again...")

def hello(name):
    print("Hi, {}!".format(name))

name = "Bob"

hello(name)

def plusOne(number):
    return number+1

num = 5

print(str(num) + " plusOne = " + str(plusOne(num)))

print("~"*30+"\n")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain."
    elif answerNumber == 2:
        return "It is decidely so."
    elif answerNumber == 3:
        return "Yes."
    elif answerNumber == 4:
        return "Reply hazy try again."
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again."
    elif answerNumber == 7:
           return "My reply is NO."
    elif answerNumber == 8:
           return "Outlook not so good."
    elif answerNumber == 9:
           return "Very doubtful."

print("The answer to your question is: {}".format(getAnswer(random.randint(1,9))))

print("~"*30+"\n")

def spam(divideBy):
    return 42 / divideBy

for num in [10,4,7,2,0,1]:
    try:
        print(spam(num))
    except ZeroDivisionError:
        print("Div0 Dumbass...")

print("~"*30+"\n")

