#!/usr/local/bin/python3

# Chapter 7 - Regular expressions

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 415-555-4242. Your number is 415-555-5858')

print('Phone number found: ' + mo.group())


