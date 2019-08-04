#!/usr/local/bin/python3

# Chapter 7 - Regular expressions

import re

#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#mo = phoneNumRegex.search('My number is 415-555-4242. Your number is 415-555-5858')

numbers = re.search((r'\d\d\d-\d\d\d-\d\d\d\d'), 'My number is 415-555-4242. Your number is 415-555-5858')

print(numbers)

#print('Phone number found: ' + mo.group())

