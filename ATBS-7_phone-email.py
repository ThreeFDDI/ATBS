#!/usr/local/bin/python3

# ATBS-7_phone-email.py
# Chapter 7 Project - extract all phone numbers and email addresses from clipboard text

import pyperclip, re

# phone regex search
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# email regex search
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # TLD
)''', re.VERBOSE)

# import clipboard text
text = str(pyperclip.paste())

# initialize list of matches 
matches = []

# search text for phone numbers
for groups in phoneRegex.findall(text):
    # format the area code + phone number
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    # add extension if found
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    # add match to the list of matches
    matches.append(phoneNum)

# search text for email addresses
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# print matches and send to clipboard
if len(matches) > 0:
    matches_out = "\n".join(matches)
    pyperclip.copy(matches_out)
    print("Copied to clipboard:")
    print(matches_out)