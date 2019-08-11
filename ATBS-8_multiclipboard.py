#!/usr/local/bin/python3

# multiclipboard saves and loads text to and from the clipboard

# Usage: py ATBS-8_multiclipboard.pyw save <keyword> saves clipboard to keyword
# Usage: py ATBS-8_multiclipboard.pyw  <keyword> loads keyword to clipboard
# Usage: py ATBS-8_multiclipboard.pyw list loads all keywords to clipboard

import shelve, pyperclip, sys

# open mcb shelf file
mcbShelf = shelve.open("mcb")

# save clipboard contents to mcb shelf
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print("Saving....")
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# delete entry from mcb shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]] 

# delete all entries
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    for k in mcbShelf.keys():
        del mcbShelf[k] 

# list all entries OR load entry into clipboard
elif len(sys.argv) == 2:   
    # list keywords and load content
    if sys.argv[1].lower() == "list":
        print(str(list(mcbShelf.keys())))
        pyperclip.copy(str(list(mcbShelf.keys())))
    # load entry into clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# close mcb shelf file
mcbShelf.close()