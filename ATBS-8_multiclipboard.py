#!/usr/local/bin/python3

# multiclipboard saves and loads text to the clipboard

# Usage: py ATBS-8_multiclipboard.pyw save <keyword> saves clipboard to keyword
# Usage: py ATBS-8_multiclipboard.pyw  <keyword> loads keyword to clipboard
# Usage: py ATBS-8_multiclipboard.pyw list loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# save clipboard contents
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print("Saving....")
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    pass
    
    # list keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
