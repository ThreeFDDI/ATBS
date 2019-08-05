#!/usr/local/bin/python3

# ATBS-7_phone-email.py
# Chapter 7 Project - extract all phone numbers and email addresses from clipboard text

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\d{3}\))?                # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.