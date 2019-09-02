#!/usr/local/bin/python3

# Chapter 16 – Sending Email and Text Messages

# ATBS-16-2.py 

from twilio.rest import Client

accountSID =    ''

authToken =     ''

myNumber =      '+1574514xxxx'

twilioNumber =  '+1574707xxxx'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

textmyself('Hey... got any pony pics??')
