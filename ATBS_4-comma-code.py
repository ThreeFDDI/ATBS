#!/usr/local/bin/python3

def makeSentence(things):
    sentence = []
    for i in range(len(things)):
        if i == len(things) - 1:
            sentence.append(" and " + things[i])

        elif i == len(things) - 2:
            sentence.append(things[i])
            
        else:
            sentence.append(things[i] + ", ")
    
    return sentence        

spam = ["apples", "bananas", "tofu", "knives", "cats"]

print("".join(makeSentence(spam)))
