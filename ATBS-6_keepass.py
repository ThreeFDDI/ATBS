#!/usr/local/bin/python3

# ATBS-6_keepass.py - A totally insecure password safe

import sys, pyperclip

# Password dictionary
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# Error if too many or too 
if len(sys.argv) != 2:
    print("\nUsage: ATBS-6_keepass.py [account]\n\nAccount password will be copied to the clipboard.")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")

else:
    print("Account not found.")
